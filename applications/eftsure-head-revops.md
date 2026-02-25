# Eftsure - Head of Revenue Operations

## Full Application Answers

**Job Link**: https://careers.eftsure.com/jobs/7259090-head-of-revenue-operations

---

## Question 1: Tell us about your experience leading a global GTM function of 100+ people

Let me tell you a story.

Two years ago, I walked into Penbrothers as Head of Sales. Beautiful office, ambitious leadership, 30+ countries, remote-first team. But there was a problem: nobody could explain where deals actually came from.

The first month, I didn't touch a single dashboard. I sat in on calls. I watched the reps. I asked questions nobody had asked before.

What I found was familiar. Classic startup chaos. A CRM full of beautiful records that nobody trusted. Forecasts that were really just wishes wrapped in confidence. A sales team that was busy — but not effective.

So I rebuilt everything.

I redesigned the entire outbound engine from scratch. We went from generic cold emails to AI-automated sequences that actually felt personal — at scale. I built territories and segmentation based on data, not gut feeling. I created a forecasting model that transformed revenue from "hopefully somewhere around $X" to "here's exactly what we'll close and why."

The result? **3x revenue in 12 months.**

But here's what most people miss: the system wasn't the hard part. The hard part was culture.

I built a coaching culture where every single rep knew their numbers, understood their gap, and knew exactly what to do next. No heroics. No miracles. Just execution.

Beyond Penbrothers, I've spent years mentoring over 250 startups through programs like 500 Startups, Plug and Play, and Startup Bootcamp. You want to know what every single scaling SaaS struggles with? Three things:

1. **Pipeline mystery** — "Where did the deal go?"
2. **CRM decay** — Garbage in, garbage out
3. **Forecast fantasy** — Wish-casting instead of data-driven decisions

I've solved each of these. At scale. Across regions. In remote-first environments.

---

## Question 2: Describe your HubSpot experience

I don't just "use" HubSpot. I treat it as the operating system for revenue.

At Penbrothers, I implemented HubSpot from the ground up:

- Built automated outbound sequences that converted at **3x the industry average** — personalized at scale, not the spray-and-pray approach most companies fall into
- Created lead scoring models based on behavioral signals, not just demographic guesswork
- Designed pipeline automation that handled stage progression, task creation, and alert workflows automatically
- Integrated with sales intelligence tools like ZoomInfo, Apollo, and Clearbit for real-time enrichment
- Established CRM hygiene as absolutely non-negotiable — weekly data audits, field compliance checks, duplicate management

But here's my philosophy, and it's served me well:

**HubSpot is a mirror, not a magic box.**

If your CRM is messy, your revenue is messy. I've watched companies spend $50,000 on tools when their data hygiene was worth $0. My approach is always the same: fix the foundation first, then layer on automation.

I also run a blog called The Unicorn Playbook where I share RevOps frameworks and HubSpot setups that founders actually use. When you've seen what works and what doesn't across 250+ startups, you develop a pretty clear sense of what matters and what doesn't.

---

## Question 3: How do you approach forecasting and revenue analytics?

Here's an uncomfortable truth: most forecasts are really just opinions dressed up in data clothing.

My approach is different. I use what I call the **Commit-Expected-Best** model:

- **COMMIT**: What the rep is 100% confident will close — signed contract, verbal agreement, the works
- **EXPECTED**: Weighted probability based on deal stage, rep history, and deal health
- **BEST**: The upside scenario — competitive win, unexpected expansion, lucky break

I build this directly into HubSpot with custom fields and roll-ups. Every week, everyone knows exactly what the number is. Not "somewhere between $50,000 and $500,000." A specific number, with specific confidence.

At Penbrothers, this forecast model was a key driver of the 3x revenue growth. When leadership knows what to expect, they can plan. Investors can trust the numbers. The team can focus on what actually moves the needle.

I also use advanced Excel and Google Sheets for scenario modeling — capacity planning, territory analysis, quota allocation. But the key principle is always the same: **the model should tell you what to do, not just what happened.**

---

## Question 4: Why Eftsure?

Two reasons:

**One: The problem matters.**

B2B payment fraud is a $5 trillion problem. Every company — every single one — is one fraudulent invoice away from disaster. This isn't "nice to have" security software. It's existential. When the problem is real, the motivation is real. I want to work on things that matter.

**Two: The inflection point is exciting.**

Eftsure is scaling from regional to global. That's my favorite phase. It's where the GTM engine needs to go from "working locally" to "working everywhere." Every region has different rhythms, different regulations, different buyer behaviors. Building a unified yet flexible system across Australia, the US, and Europe — that's exactly the kind of architecture challenge I'm built for.

And look, I'm based in Tokyo. I understand time zones. I've operated globally my entire career. They don't scare me. They just require better systems. And I've spent a decade building remote-first sales engines that work regardless of geography.

---

## Question 5: Salary expectations

Market rate for this level. I'm happy to discuss based on the full compensation package — base, equity, benefits. I'm looking for a role where I can build something, not just optimize something.

---

## Question 6: Notice period

Two weeks. I'm not sitting on anything. When the right opportunity comes, I'm ready to move.

---

## Question 7: Work visa / Location

Portuguese citizen. No visa required for most work contexts. I'm based in Tokyo, Japan (JST timezone), and I'm happy to be hybrid from the Sydney office as needed. The Australia timezone is very manageable from Tokyo — I've worked with teams across Asia, Europe, and the Americas for years.

---

## Automation Ideas I'd Bring

Here's what I'd tackle in my first 30 days — with full step-by-step tutorials:

---

### AUTOMATION 1: Multi-Region Lead Routing Engine

#### THE PROBLEM

Eftsure operates across three regions: Australia (Sydney), US (Dallas), and Europe (France). When a new lead comes in, there's no standardized way to route it to the right rep at the right time. The result:

- Leads in the wrong time zone get contacted during their off-hours
- Follow-up sequences are all the same regardless of region buying patterns
- No consideration for regional holidays, business hours, or cultural differences
- Response times suffer because nobody "owns" the lead immediately

#### THE IDEA

Build a HubSpot workflow that automatically:

1. **Detects** the lead's geography (from domain, country field, or enrichment data)
2. **Routes** the lead to the correct regional queue
3. **Triggers** a region-specific follow-up sequence with timing that matches local business hours
4. **Enriches** the lead with company data (employee count, industry, revenue) to help the rep prioritize

This sounds simple but it's incredibly powerful — it means every lead gets a personalized experience from second one.

#### STEP-BY-STEP TUTORIAL

**Prerequisites:**}
**Prerequisites:**
- HubSpot Professional or above (for workflow automation)
- Clearbit or ZoomInfo account (for enrichment)
- At least 3 sales reps or teams across regions

**Step 1: Set up Regional Properties**
In HubSpot, create these custom properties:
- `region` (dropdown): Australia, US, Europe, Other
- `local_business_hours` (single-line text): Store the lead's local timezone
- `routing_owner` (owner): Assign to regional sales rep

**Step 2: Create the Routing Workflow**
Go to HubSpot → Automations → Workflows → Create workflow (Contact-based)

```
TRIGGER:
- Form submission
- OR Manual list upload
- OR Import

ACTION 1: Enrich Contact (Clearbit/ZoomInfo)
- Pull company name, domain, employee count, industry, revenue

ACTION 2: Set Regional Property
- If company domain ends in .au → Set region = Australia
- If company domain ends in .com, .org (US-based) → Set region = US  
- If company domain ends in .co.uk, .de, .fr, etc → Set region = Europe
- Else → Set region = Other

ACTION 3: Set Owner Based on Region
- If region = Australia → Set owner to Sydney Rep
- If region = US → Set owner to Dallas Rep
- If region = Europe → Set owner to France Rep

ACTION 4: Set Local Business Hours
- Use a simple formula or lookup table:
  - Australia: "9am-6pm AEST"
  - US: "9am-6pm CST" 
  - Europe: "9am-6pm CET"

ACTION 5: Add to Regional Sequence
- If region = Australia → Enroll in "AU Follow-up Sequence"
- If region = US → Enroll in "US Follow-up Sequence"
- If region = Europe → Enroll in "EU Follow-up Sequence"

ACTION 6: Create Task for Rep
- Task: "Follow up with [Company Name] - [Region]"
- Due: Now + [region-specific delay]
- Priority: High/Medium based on company size
```

**Step 3: Create Region-Specific Email Sequences**

Create 3 separate email sequences (HubSpot → Sales Email → Sequences):

**AU Sequence:**
- Email 1: Send immediately (their morning = your evening)
- Email 2: Wait 2 days, send at 9am AEST
- Email 3: Wait 3 days, send at 9am AEST

**US Sequence:**
- Email 1: Send immediately (their morning)
- Email 2: Wait 2 days, send at 9am CST
- Email 3: Wait 3 days, send at 9am CST

**EU Sequence:**
- Email 1: Send immediately (their morning = your night)
- Email 2: Wait 2 days, send at 9am CET
- Email 3: Wait 3 days, send at 9am CET

**Step 4: Test and Refine**
- Run 10 test leads through the workflow
- Check that each gets assigned to the correct owner
- Verify emails send at the right local times
- Adjust based on open rates and response times

**Expected ROI:**
- 20-30% faster first response time
- 15% higher conversion on first touch
- 0% lead routing errors (no manual assignment needed)

**Time to build:** 2-4 hours

---

### AUTOMATION 2: CRM Hygiene Automation Suite

#### THE PROBLEM

With 100+ people using HubSpot, data quality decays fast:

- **Duplicates**: Same company entered multiple times with slight variations (e.g., "Acme Corp" vs "Acme Corporation" vs "acme corp")
- **Incomplete records**: Contacts without email, phone, company, or any useful info
- **Stale data**: Deals and contacts that haven't been touched in 30+ days but still active
- **Field inconsistency**: Wrong formats, typos, inconsistent use of picklist values

The result? Garbage in, garbage out. Forecasts become useless. Reports don't match reality. Reps waste time on bad data.

#### THE IDEA

Build a suite of automated hygiene workflows that run on schedule:

1. **Duplicate detection and merge**: Automatically find and flag potential duplicates for review
2. **Data completeness scoring**: Score every contact/company on how complete they are, flag incomplete ones
3. **Stale record detection**: Identify records that haven't been updated in 30+ days
4. **Field validation**: Ensure email formats are valid, phone numbers are correct, etc.

This is not glamorous work but it's the foundation of every high-performing RevOps function.

#### STEP-BY-STEP TUTORIAL

**Prerequisites:**
- HubSpot Professional or above
- No additional paid tools needed (HubSpot has built-in duplicate detection)

---

**Part A: Duplicate Detection**

**Step 1: Enable Duplicate Detection**
HubSpot has built-in duplicate detection. Go to:
Settings → Data Management → Duplicates → Enable

**Step 2: Create a Weekly Duplicate Review Workflow**
```
TRIGGER:
- Weekly schedule (every Monday at 9am)

ACTION 1: Find Duplicate Contacts
- Use "Has duplicate email" or "Has duplicate company"

ACTION 2: Create Task for Sales Ops
- Task: "Review [X] duplicate contacts"
- Assign to: RevOps owner
```

**Step 3: Manual Merge Process**
For each flagged duplicate:
- Go to contact record
- Click "Merge" 
- Keep the record with more complete data
- HubSpot will merge all associated deals, notes, emails

---

**Part B: Data Completeness Scoring**

**Step 1: Create Custom Properties for Scoring**

Create a number property called `data_completeness_score` on contacts.

**Step 2: Create the Scoring Workflow**
```
TRIGGER:
- Contact created
- OR Contact property changed (any property)

CALCULATE SCORE:
Set data_completness_score to:
- +20 if email is valid
- +20 if phone exists
- +20 if company is associated
- +20 if job title exists
- +20 if country/region is set

(0-100 scale, higher = more complete)
```

**Step 3: Flag Incomplete Contacts**
```
TRIGGER:
- Weekly schedule

ACTION 1: Filter contacts where data_completeness_score < 50

ACTION 2: Create task for owner
- Task: "Complete contact record for [name]"
- Due: 3 days from now

ACTION 3: Add to "Needs Attention" list
- Add to static list for RevOps review
```

---

**Part C: Stale Record Detection**

**Step 1: Create "Last Activity" Properties**
Use HubSpot's built-in "Last Activity Date" property, or create custom:
- `days_since_last_contact`
- `days_since_last_deal_update`

**Step 2: Stale Deal Workflow**
```
TRIGGER:
- Weekly schedule

ACTION 1: Filter deals where:
  - Deal stage is not "Closed Won" or "Closed Lost"
  - AND Days in current stage > 30
  - AND Last activity date > 30 days ago

ACTION 2: Create task for owner
- Task: "Review stale deal: [Deal Name]"
- Due: 2 days

ACTION 3: Change deal stage to "At Risk" (or similar)
- Add property "stale_reason": "No activity in 30+ days"
```

---

**Part D: Field Validation**

**Step 1: Create Validation Workflow**
```
TRIGGER:
- Contact property changed (email, phone)

ACTION 1: If email doesn't match regex pattern
- Set property "email_valid": false
- Create task: "Verify email format for [name]"

ACTION 2: If phone doesn't match patterns
- Set property "phone_valid": false
- Create task: "Verify phone for [name]"
```

**Step 2: Use HubSpot's Data Quality Automation**
Settings → Data Management → Data Quality Automation → Enable
- This automatically validates email formats and flags hard bounces

---

**Expected ROI:**
- 50% reduction in duplicate records
- 30% improvement in contact completeness
- Earlier detection of stale deals (before they go cold)
- Cleaner data = reliable forecasts

**Time to build:** 3-5 hours

---

### AUTOMATION 3: Cross-Region Forecasting Dashboard

#### THE PROBLEM

Eftsure has three regions with:
- Different}
Eftsure has three regions with:
- Different fiscal calendars (could be different quarters)
- Different currencies (AUD, USD, EUR)
- Different sales cycles and deal sizes
- Different teams with different forecasting habits

Currently, there's no unified view of pipeline health across all regions. Leaders have to manually pull reports from each region and try to combine them in Excel. It's slow, error-prone, and doesn't give real-time visibility.

#### THE IDEA

Build a unified forecasting dashboard that:

1. **Rolls up** all deals from all regions into one view
2. **Segments** by region with one-click filtering
3. **Shows** Commit-Expected-Best for each region and total
4. **Alerts** automatically when deals stall, slip, or get stuck
5. **Projects** end-of-quarter forecasts based on current velocity

This gives leadership the exact number they need — not "somewhere between $X and $Y" but "we will close $X, we expect $Y, and best case is $Z."

#### STEP-BY-STEP TUTORIAL

**Prerequisites:**
- HubSpot Professional or above (for custom properties and reports)
- Google Sheets or Excel for advanced modeling
- Optional: Tableau, Looker, or HubSpot Analytics for visualization

---

**Part A: Set Up Forecast Custom Properties**

Create these properties on the Deal object:

1. **`forecast_category`** (single select):
   - Commit
   - Expected
   - Best
   - Pipeline (just potential, not weighted)

2. **`close_probability`** (number, 0-100):
   - Manual or automatic based on deal stage
   - Use "Default probability" in deal stages settings

3. **`region_pipeline`** (single select):
   - Australia
   - US
   - Europe

4. **`last_forecast_update`** (date):
   - Auto-update when forecast_category changes

5. **`forecast_notes`** (multiline text):
   - Rep's reasoning for their forecast

---

**Part B: Create the Regional Roll-Up Report**

**Step 1: Build Individual Region Reports**
In HubSpot, create saved views for each region:

- Australia Pipeline: Filter by region_pipeline = Australia, deal stage not in Closed
- US Pipeline: Filter by region_pipeline = US, deal stage not in Closed
- Europe Pipeline: Filter by region_pipeline = Europe, deal stage not in Closed

**Step 2: Create a Pipeline Dashboard**
HubSpot → Reports → Dashboards → Create Dashboard

Add these report blocks:

```
Block 1: Total Pipeline Value
- All deals (excluding closed)
- Sum of amount

Block 2: Pipeline by Region (pie chart)
- Group by region_pipeline
- Sum of amount

Block 3: Forecast by Category (bar chart)
- Group by forecast_category
- Sum of amount

Block 4: Deals Closing This Month
- Close date = this month
- Group by deal stage
- Sum of amount

Block 5: Weighted Forecast
- Formula: (Commit × 100% + Expected × 75% + Best × 50%) / 3
- Display as single number
```

**Step 3: Add Deal Velocity Metrics**
Create a custom report:
- Average time from created to close (by region)
- Average time in each stage (by region)
- Win rate by region

---

**Part C: Build the Google Sheets Forecast Model**

For more advanced forecasting, connect HubSpot to Google Sheets:

**Step 1: Install HubSpot Google Sheets Add-on**
HubSpot App Marketplace → HubSpot for Sheets → Install

**Step 2: Create Weekly Export**
Set up automated weekly export of:
- All open deals with: name, amount, stage, close date, owner, region, forecast_category

**Step 3: Build Forecast Tab**
In Google Sheets, create tabs:

```
Tab 1: Raw Data (paste from HubSpot export)

Tab 2: Regional Summary
- AU: =SUMIF(region, "Australia", amount)
- US: =SUMIF(region, "US", amount)  
- EU: =SUMIF(region, "Europe", amount)
- Total: =SUM(amount)

Tab 3: Forecast Calculation
- Commit: =SUMIF(forecast, "Commit", amount)
- Expected: =SUMIF(forecast, "Expected", amount)
- Best: =SUMIF(forecast, "Best", amount)
- Weighted: =(Commit*1 + Expected*0.75 + Best*0.5)

Tab 4: Scenario Modeling
- Conservative: Commit only
- Base case: Weighted
- Optimistic: Best case

Tab 5: Velocity Analysis
- Deals closing this month
- Deals closing next month
- Deals closing this quarter
- Run rate: (closed this month) / (days elapsed) × (days in month)
```

**Step 4: Create Charts**
- Line chart: Forecast over time (weekly snapshots)
- Bar chart: Commit vs Expected vs Best by region
- Waterfall: Pipeline → Commit → Closed

---

**Part D: Set Up Automated Alerts**

**Step 1: Deal Stalled Alert**
```
TRIGGER:
- Deal stage hasn't changed in 14 days
- AND Deal amount > $10,000

ACTION:
- Email to deal owner: "Deal stalled: [Deal Name]"
- Create task: "Revisit [Deal Name] - no movement in 14 days"
- Notify RevOps in Slack/email
```

**Step 2: Deal Slip Alert**
```
TRIGGER:
- Close date moved out by more than 7 days
- AND Deal amount > $10,000

ACTION:
- Email to deal owner: "Deal slipped: [Deal Name]"
- Log: Old close date vs new close date
- Create task: "Confirm new timeline for [Deal Name]"
```

**Step 3: Forecast at Risk Alert**
```
TRIGGER:
- Weekly schedule
- AND (Commit total < 80% of quota)

ACTION:
- Email to Sales Leader: "Forecast at risk: Commit is [X]% of quota"
- Include: Top 5 at-risk deals by amount
```

---

**Expected ROI:**
- Real-time visibility into pipeline across all regions
- No more manual spreadsheet combining
- Earlier detection of at-risk deals
- More accurate forecasting (data-driven, not guess-driven)
- Leadership can make decisions faster

**Time to build:** 4-6 hours

---

## Summary

These three automations solve the most common RevOps problems:

1. **Lead Routing** — Get leads to the right people at the right time, automatically
2. **CRM Hygiene** — Keep your data clean so your forecasts are trustworthy
3. **Forecasting Dashboard** — Know exactly what you'll close, by region, every week

All three can be built in a total of 9-15 hours (2-4 + 3-5 + 4-6).

They demonstrate immediate value, require no additional tools beyond what Eftsure likely already has, and set the foundation for a world-class RevOps function.
