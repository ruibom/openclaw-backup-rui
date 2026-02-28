## Inbound Lead Workflow (triggered when Rui pastes an email or introduction)

Activate automatically when Rui pastes a message, email, or introduction in any Apex channel. Run the full pipeline without being asked. No prompting needed.

### Step 1 — Extract
Identify: person's name and role, their company, the opportunity described, what they are looking for, and how they reached Rui (intro, cold email, LinkedIn, etc.).

### Step 2 — Score
If the inbound message describes a specific job role, load CAREER_PROFILE.md and score using the standard 5-criteria algorithm. If it is a referral intro, networking call, or advisory conversation with no explicit role — skip scoring entirely and proceed directly to Step 3. Do NOT apply the job scoring rubric to networking calls.

### Step 3 — Research
Use web_search and web_fetch to research both the company and the person. NEVER use the Chrome browser tool. Search the person by full name independently from the company — do not assume their primary role matches the email domain. Cross-reference their name with known companies, LinkedIn, and recent news to find their actual background:

Company:
- Funding stage and total raised
- Headcount and growth trajectory
- Product and core value proposition
- Recent news, hires, or announcements
- Leadership team and their backgrounds
- Glassdoor signals (culture, red flags)
- Top 2 competitors and how this company differentiates from them

Person:
- LinkedIn profile: background, career path, how long at this company
- Why they reached out to Rui specifically — mutual connection, saw his content, referral
- Their hiring patterns or previous hires if visible
- Any public writing, posts, or interviews that reveal what they value

### Step 4 — Interview Prep Package
Load CAREER_PROFILE.md and LINKEDIN_VOICE.md fully. Read both before writing a single word of the prep. Everything produced must sound like Rui — operator-first, fragment-heavy, brutally honest, dry wit. Never corporate. Never fluffy.

Internalize before writing:
- Builder identity: systems, teams, momentum — not a manager, an operator
- Edge: sales strategy + zero-to-one team building + brutally practical GTM execution
- Proof points: 3x revenue in 12 months at Penbrothers (rebuilt entire GTM end-to-end), co-founder x2, raised $1M early-stage, 250+ startups mentored at 500 Startups, built life from scratch in China then Japan with no network
- Ambition: founder-adjacent or portfolio-style leadership, structure-from-ambiguity, helping multiple businesses move from momentum to repeatability
- Non-negotiables: fully remote, 250K+ USD, Series B-C, APAC-friendly
- Cross-reference LINKEDIN_VOICE.md for tone before drafting any answer or question

Produce the following:

**1. COMPANY BRIEF**
One tight paragraph: what they do, stage, why they are hiring now, what matters to them culturally and commercially.

**2. PERSON BRIEF**
Who this person is, their angle, what they care about, what Rui should know before talking to them. Any rapport hooks from their background.

**3. ROLE FIT MAP**
For each thing they are looking for, map Rui's exact experience to it. Use specifics — not "I have GTM experience" but "At Penbrothers I rebuilt the entire sales motion from scratch and tripled revenue in 12 months." Pull directly from CAREER_PROFILE.md.

**4. LIKELY QUESTIONS**
Top 5-7 questions they will ask based on the role, company context, and research from Step 3. For each: write Rui's suggested answer in his voice — direct, story-driven, proof-point-anchored.

**5. QUESTIONS TO ASK THEM**
3-5 sharp questions Rui should ask that signal operator-level thinking. These should make the interviewer feel like Rui has already been thinking about their problems.

**6. RED FLAGS**
Anything in the company, role, comp structure, or person's message that warrants caution. Be direct — if something looks off, say so.

**7. AUTOMATION TALKING POINTS**
Generate 2-3 specific AI or automation plays Rui can drop naturally in the conversation to make the interviewer think "we need this person now." Calibrate these to what THIS company needs based on Steps 2-3 research — outbound engine for sales roles, pipeline scoring for GTM roles, RevOps dashboards for ops roles, mentoring-at-scale systems for leadership roles.

Each automation play must be structured as:

WHAT: what the automation does in one sentence
HOW: the specific tools, stack, or method (name them — be concrete)
WHY: the business outcome it drove or would drive, with metrics where possible
HOW TO EXECUTE: 3-4 step deployment plan they could actually run at their company starting next week

Frame these as stories Rui tells naturally in conversation, not slides he reads. Example opening: "One thing I built at Penbrothers was a fully AI-automated outbound engine..." Ground every play in Rui's actual experience: Penbrothers outbound engine, AI-automated pipelines with Philippines-based teams, Discord-based multi-agent AI system, startup mentoring infrastructure at 500 Startups, co-founder GTM from zero.

**8. OBJECTION HANDLING (Reverse SWOT)**
Identify 2-3 specific reasons they might not hire Rui based on the research and role context. Common ones: too entrepreneurial, expects too much autonomy, cost basis, no direct industry vertical experience. For each objection:
- STATE IT honestly — do not sugarcoat
- PIVOT IT in Rui's voice — turn the weakness into a feature or an unfair advantage
- Example: "Too entrepreneurial" → "I'm not here to be a passenger. I want founder-level skin in the game, which means I'll move faster and care more than anyone you hire off a corporate track."
These are rehearsed, not improvised. Rui should know them cold before the call.

**9. FIRST 90-DAY WEDGE**
Based on the company research in Step 3, identify the one most obvious broken or underbuilt system — slow pipeline, weak outbound, no RevOps infrastructure, poor lead response time, missing enablement layer. Propose a specific "Day 1 audit" Rui can name drop in the interview:
- WHAT is broken (name it specifically using their own Glassdoor/news signals)
- WHAT Rui would do in the first 30 days to start fixing it (specific system or tool)
- WHAT the measurable outcome would look like by Day 90
Frame this as a hypothesis, not a promise: "Based on what I've seen, my first move would be..." This makes them feel like he's already solving their problems before he's hired.

**10. CULTURAL VIBE CHECK (Anti-Pattern Detection)**
Rui has a very specific operating identity. Screen them as hard as they screen him. Based on role and company research, flag 2-3 specific things to listen for that would trigger an immediate no:
- Language signals: if they say "consensus," "alignment," "stakeholder buy-in" more than "momentum," "ship," "revenue" — wrong environment
- Process signals: if they have no CRM, no pipeline data, or "we're still figuring out our ICP" at Series B — chaos without upside
- Autonomy signals: if every decision requires committee approval or a 6-week procurement cycle — wrong fit
For each anti-pattern, give Rui a sharp clarifying question he can ask to surface it naturally in conversation without tipping his hand.

**11. COMPETITIVE INTELLIGENCE**
Research the top 2 competitors to this company. Give Rui one sharp talking point on why this company's approach is differentiated — or where it is at risk. Frame it as owner-level thinking: "I looked at how you compare to X and Y, and the thing that stands out is..." This signals he's thinking like an investor, not an applicant. If the company's position looks weak relative to competitors, flag it as a red flag in Section 6.

### Step 5 — Reply Draft
If the message requires a reply, draft one in Rui's voice: warm, direct, confident, no fluff. Express genuine interest if the score warrants it. Ask one sharp clarifying question if needed.

### Step 6 — Log and Notion
Save full prep package to APPLICATION_LOG.md with date and company slug.

Follow the Notion Workspace workflow defined at the bottom of this file:
1. Create Interview Prep page under Interview Prep folder (ID in Notion Workspace section). Title: "{Company} — Interview Prep". Paste full prep package as page content. Record its URL.
2. Create row in Job Applications Tracker using exact field names from the Notion Workspace section:
   - Company: company name
   - Role: role title
   - Score: score out of 10 from Step 2 (leave 0 if networking call with no role)
   - Job Link: paste the original message URL or "Inbound intro" if no URL
   - Contact Person: name, role, and LinkedIn URL of the person who reached out
   - Notes: 2–3 sentence summary from Step 3 research
   - Source: Inbound Referral
   - Status: RESEARCH
   - Interview Prep: URL of the page created in step 1
3. Post ONLY the mandatory Discord output format defined in the Notion Workspace section. Never post the full brief in Discord.

---

## Post-Interview Workflow (triggered when Rui shares interview feedback or transcript)

Activate when Rui pastes a meeting transcript, voice memo summary, or written debrief after an interview. Run automatically — no prompting needed.

### Step 1 — Debrief Analysis
Read the transcript or feedback fully. Extract:
- What topics came up that were not in the prep package
- How Rui's answers landed (based on his own assessment or transcript signals)
- What the interviewer seemed most excited about
- What felt flat, unclear, or unresolved
- Any new information about the role, comp, team, or company that was not in the research

### Step 2 — Sentiment Read
Based on the transcript or Rui's feedback, give an honest read on where things stand:
- Strong positive signals (they mentioned next steps, intro'd to another person, asked about start date)
- Neutral or unclear signals (polite but noncommittal)
- Negative signals (short answers, no next steps mentioned, probing questions on weaknesses)
- Overall: Green / Amber / Red with one sentence of reasoning

### Step 3 — Gap Analysis
Compare what actually happened in the interview against the prep package. Flag:
- Any objections that came up that were not anticipated in Section 8
- Any questions Rui did not answer as strongly as he could have — suggest a sharper version now
- Anything Rui should have said but did not get a chance to — this becomes the follow-up artifact

### Step 4 — Post-Interview Value-Add Strike
Draft a follow-up message for Rui to send within 24 hours. This is NOT a thank-you note. It is a value-add artifact built directly from what came up in the interview.

Structure:
- HOOK: reference one specific thing they discussed — use the actual topic from the transcript (e.g., "You mentioned lead response time being the biggest gap right now...")
- ARTIFACT: a concrete thing Rui is sending — choose the most relevant:
  - A rough automation map for the stack they discussed
  - A 2-3 bullet "Day 1 audit" framework for the specific problem they raised
  - A Loom script Rui can record (write the exact script, 90 seconds max)
  - A one-page mini-doc summarizing the system Rui would build for their exact situation
- CLOSE: one sentence, no fluff — "Happy to go deeper on any of this when you're ready."

Tone: warm, direct, operator. Not grateful. Not desperate. Peer to peer.

### Step 5 — Next Move
Based on the sentiment read, tell Rui exactly what to do next:
- Green: send the value-add within 24h, propose specific next step
- Amber: send the value-add, ask one sharp question to re-engage
- Red: assess whether to invest further or deprioritize, suggest honest framing

### Step 6 — Log and Notion Update
Append debrief summary, sentiment read, and follow-up draft to APPLICATION_LOG.md under the same company slug.

Follow skill: ~/.openclaw/workspace/skills/notion.md
Update the existing Notion entry for this company using the same job dashboard fields:
- Interview Notes: append interview debrief summary and sentiment read (Green/Amber/Red)
- Status: update to reflect current stage — INTERVIEW DONE / FOLLOW-UP SENT / OFFER / CLOSED
- Application Answers: if a follow-up artifact was created, save it to GitHub and update the raw URL here

Status progression for all job leads (inbound and outbound):
RESEARCH → APPLIED → INTERVIEW SCHEDULED → INTERVIEW DONE → FOLLOW-UP SENT → OFFER → CLOSED (hired or rejected)

Always update Notion status at every stage transition. Never let the dashboard fall behind reality.
