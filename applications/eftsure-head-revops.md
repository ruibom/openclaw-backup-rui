# Eftsure - Head of Revenue Operations

## Application Answers

---

### Q1: Experience leading global GTM (100+ people)

I led Sales at Penbrothers, a B2B SaaS platform in the Philippines. When I joined, the sales operation was ad-hoc - no real process, no forecasting, CRM was a data graveyard.

In 12 months, I:
- Rebuilt the entire outbound engine (sequences, messaging, automation)
- Designed territories and segmentation from scratch
- Built a forecasting model that actually worked - went from "hope" to data-driven
- Result: 3x revenue growth

I also mentored 250+ startups through 500 Startups and Plug and Play. Every single one struggled with the same 3 things: pipeline mystery, CRM decay, and forecast fantasy. I've solved all three at scale.

I'm comfortable leading distributed teams across time zones - Penbrothers had reps in 30+ countries.

---

### Q2: HubSpot experience

I've used HubSpot extensively - implemented it from ground up at Penbrothers.

What I actually did:
- Built automated outbound sequences (converted 3x industry average)
- Created lead scoring models based on behavior, not just demographics
- Set up pipeline automation (stage progression, task creation, alerts)
- Integrated with ZoomInfo, Apollo, Clearbit for enrichment
- Enforced CRM hygiene - weekly audits, field compliance

My philosophy: HubSpot is a mirror. If your data is messy, your revenue decisions are bad. Fix the foundation first, then automate.

---

### Q3: Forecasting approach

I use a Commit-Expected-Best model:

- **Commit**: 100% confident will close (verbal/signed)
- **Expected**: Weighted by stage, rep history, deal health
- **Best**: Upside scenario

Built this in HubSpot with custom fields. Every week, we knew exactly what we'd close - not a range.

At Penbrothers, this was a key driver of the 3x growth. Leadership trusted the numbers. Investors trusted the numbers.

Also use advanced Excel/Sheets for scenario modeling - capacity planning, territory analysis, quota allocation.

---

### Q4: Why Eftsure?

Two reasons:

1. The problem is real. B2B payment fraud is a $5T problem. Every company is one fraudulent invoice away from disaster. That's meaningful.

2. The inflection point. Going from regional (AU) to global (US, EU) is exactly the phase I thrive in. Building a unified but flexible GTM system across regions is what I do.

Location: Based in Tokyo. Time zones don't scare me - I ran a global team from here.

---

### Q5: Salary expectations

Market rate for this level. Happy to discuss based on full package (base, equity, benefits).

---

### Q6: Notice period

2 weeks.

---

### Q7: Location/Visa

Portuguese citizen, no visa needed. Based in Tokyo. Happy to be hybrid from Sydney as needed - AU timezone is manageable from Japan.

---

## Automation Ideas

### Automation 1: Multi-Region Lead Routing

**What we're building:**
A HubSpot workflow that automatically routes new leads to the right regional sales team based on company location, and sets up personalized follow-up sequences that match each region's business hours.

**Why we're building it:**
When you have 3 regions (AU, US, EU), leads often get routed manually or randomly. This causes: slow response times, leads contacted during wrong hours, no regional customization. The result is lower conversion.

**What to expect:**
- Every new lead gets assigned to the right regional rep within seconds
- Follow-up emails send at appropriate local times (9am in Sydney, 9am in Dallas, 9am in Paris)
- No manual routing needed - the system does it automatically

**Step-by-step:**

1. **Create region property in HubSpot**
   - Go to Settings > Properties > Contacts > Create new
   - Name: "Region" - Type: Dropdown select
   - Options: Australia, US, Europe, Other

2. **Build the routing workflow**
   - Automations > Workflows > Create > Contact-based
   - Trigger: Form submission OR Manual list upload
   - Action 1: Use Clearbit/ZoomInfo to enrich company domain
   - Action 2: Set region property:
     - If domain ends .au → Australia
     - If domain ends .com (US company) → US  
     - If domain ends .co.uk, .de, .fr → Europe
   - Action 3: Set owner based on region (assign to AU/US/EU rep)
   - Action 4: Enroll in region-specific email sequence

3. **Create 3 email sequences (one per region)**
   - Each sequence has 3 emails
   - Set send times to match local business hours
   - Example AU: Send at 9am AEST
   - Example US: Send at 9am CST
   - Example EU: Send at 9am CET

4. **Test with 10 leads**
   - Run test data through workflow
   - Verify correct routing and timing

**Time to build:** 2-4 hours
**ROI:** 20-30% faster first response, 15% higher conversion

---

### Automation 2: CRM Hygiene Automation

**What we're building:**
A suite of automated workflows that keep your HubSpot data clean - detecting duplicates, scoring data completeness, and flagging stale records.

**Why we're building it:**
With 100+ people using CRM, data gets messy fast. Duplicates pile up, fields get abandoned, deals go stale. When your data is bad, your forecasts are bad. Garbage in, garbage out.

**What to expect:**
- Weekly automated check for duplicate contacts/companies
- Every contact gets a "completeness score" (0-100 based on filled fields)
- Deals with no activity in 30 days get flagged automatically
- Tasks created for reps to clean up their data

**Step-by-step:**

**Part A: Duplicate Detection**

1. Enable in HubSpot: Settings > Data Management > Duplicates > Enable
2. Create weekly workflow:
   - Trigger: Weekly schedule
   - Filter: Has duplicate email = yes
   - Action: Create task for Sales Ops to review and merge

**Part B: Data Completeness Score**

1. Create number property: "Data Score" (0-100)
2. Build workflow:
   - Trigger: Contact created or updated
   - Set score: +20 each for email, phone, company, job title, country
3. Second workflow:
   - Trigger: Weekly
   - Filter: Data Score < 50
   - Action: Create task for owner to complete record

**Part C: Stale Deal Detection**

1. Create workflow:
   - Trigger: Weekly
   - Filter: Deal stage not Closed, Last activity > 30 days ago, Amount > $10K
   - Action: Change stage to "At Risk", Create task for owner

**Time to build:** 3-5 hours
**ROI:** 50% fewer duplicates, 30% more complete records, earlier stale deal detection

---

### Automation 3: Cross-Region Forecasting Dashboard

**What we're building:**
A unified dashboard showing pipeline health across all regions, with Commit/Expected/Best numbers and automated alerts when forecasts are at risk.

**Why we're building it:**
Currently you probably manually pull reports from each region and combine in Excel. It's slow, error-prone, and doesn't give real-time visibility. Leaders need to know the number every week, not guess.

**What to expect:**
- One dashboard showing all regions combined
- Click to filter by region (AU, US, EU)
- See Commit, Expected, and Best numbers for each region and total
- Automated alerts when deals stall or slip
- Weekly forecast updates without manual work

**Step-by-step:**

1. **Create forecast properties on Deal object**
   - Forecast Category: Commit / Expected / Best / Pipeline
   - Region Pipeline: AU / US / EU
   - Last Forecast Update: Date

2. **Build HubSpot dashboard**
   - Reports > Dashboards > Create
   - Add: Total pipeline value (all deals)
   - Add: By region (pie chart)
   - Add: By forecast category (bar chart)
   - Add: Deals closing this mon}