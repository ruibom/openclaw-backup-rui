#!/usr/bin/env bash
# Cost Tracker - Calculate daily OpenClaw usage costs

set -e

WORKSPACE="$HOME/.openclaw/workspace"
COSTS_DIR="$WORKSPACE/costs"
PRICING_FILE="$COSTS_DIR/model-pricing.json"
LOG_DIR="$COSTS_DIR/logs"
TODAY=$(date +%Y-%m-%d)
LOG_FILE="$LOG_DIR/$TODAY.json"

# Ensure directories exist
mkdir -p "$LOG_DIR"

# Get pricing info
get_price() {
    local model=$1
    local type=$2  # input or output
    jq -r ".models.$model.${type}_cost_per_1m // 0" "$PRICING_FILE"
}

# Log current session usage
log_usage() {
    local model=$1
    local input_tokens=$2
    local output_tokens=$3
    local timestamp=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
    
    # Calculate costs
    local input_price=$(get_price "$model" "input")
    local output_price=$(get_price "$model" "output")
    local input_cost=$(echo "scale=6; $input_tokens * $input_price / 1000000" | bc)
    local output_cost=$(echo "scale=6; $output_tokens * $output_price / 1000000" | bc)
    local total_cost=$(echo "scale=6; $input_cost + $output_cost" | bc)
    
    # Create log entry
    local entry=$(jq -n \
        --arg ts "$timestamp" \
        --arg model "$model" \
        --arg input "$input_tokens" \
        --arg output "$output_tokens" \
        --arg cost "$total_cost" \
        '{
            timestamp: $ts,
            model: $model,
            tokens: {
                input: ($input | tonumber),
                output: ($output | tonumber),
                total: (($input | tonumber) + ($output | tonumber))
            },
            cost_usd: ($cost | tonumber)
        }')
    
    # Append to today's log
    if [[ -f "$LOG_FILE" ]]; then
        jq ". += [$entry]" "$LOG_FILE" > "$LOG_FILE.tmp" && mv "$LOG_FILE.tmp" "$LOG_FILE"
    else
        echo "[$entry]" > "$LOG_FILE"
    fi
    
    echo "✅ Logged: $model - ${input_tokens}in/${output_tokens}out = \$$total_cost"
}

# Calculate daily total
daily_total() {
    local date=${1:-$TODAY}
    local file="$LOG_DIR/$date.json"
    
    if [[ ! -f "$file" ]]; then
        echo "No data for $date"
        return
    fi
    
    echo "📊 Usage for $date:"
    echo ""
    
    # Per-model breakdown
    for model in kimi sonnet opus; do
        local model_data=$(jq "[.[] | select(.model == \"$model\")]" "$file")
        local count=$(echo "$model_data" | jq 'length')
        
        if [[ $count -gt 0 ]]; then
            local input=$(echo "$model_data" | jq '[.[].tokens.input] | add')
            local output=$(echo "$model_data" | jq '[.[].tokens.output] | add')
            local cost=$(echo "$model_data" | jq '[.[].cost_usd] | add')
            
            printf "  %-10s: %'8d in / %'6d out = \$%.4f\n" "$model" "$input" "$output" "$cost"
        fi
    done
    
    echo ""
    
    # Total
    local total_cost=$(jq '[.[].cost_usd] | add' "$file")
    local total_input=$(jq '[.[].tokens.input] | add' "$file")
    local total_output=$(jq '[.[].tokens.output] | add' "$file")
    
    printf "  %-10s: %'8d in / %'6d out = \$%.4f\n" "TOTAL" "$total_input" "$total_output" "$total_cost"
}

# Weekly total
weekly_total() {
    echo "📈 Last 7 days:"
    echo ""
    
    local total=0
    for i in {0..6}; do
        local date=$(date -v-${i}d +%Y-%m-%d 2>/dev/null || date -d "$i days ago" +%Y-%m-%d)
        local file="$LOG_DIR/$date.json"
        
        if [[ -f "$file" ]]; then
            local cost=$(jq '[.[].cost_usd] | add' "$file")
            printf "  %s: \$%.4f\n" "$date" "$cost"
            total=$(echo "$total + $cost" | bc)
        fi
    done
    
    echo ""
    printf "  Week total: \$%.4f\n" "$total"
    printf "  Avg/day:    \$%.4f\n" "$(echo "scale=4; $total / 7" | bc)"
}

# Main command router
case "${1:-help}" in
    log)
        log_usage "${2:-kimi}" "${3:-0}" "${4:-0}"
        ;;
    today)
        daily_total
        ;;
    week)
        weekly_total
        ;;
    help|*)
        cat <<EOF
Cost Tracker - Track OpenClaw API costs

Usage:
  cost-tracker.sh log <model> <input_tokens> <output_tokens>
  cost-tracker.sh today
  cost-tracker.sh week
  
Examples:
  cost-tracker.sh log kimi 10000 500
  cost-tracker.sh today
  cost-tracker.sh week

Models: kimi, sonnet, opus
EOF
        ;;
esac
