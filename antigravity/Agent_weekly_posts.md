
# Agent: Weekly LinkedIn Batch Generator

**Name:** `@batch-posts`
**Run Schedule:** Every Monday at 10:00 AM JST (Auto-trigger).

---

## 🔁 WHAT IT DOES (Step-by-Step)

1. **Scan Sources:** Pulls 6 topics based on the category-to-folder mapping:
   * **Real/Fictional Stories:** `/outputs_final/meetings`, `/outputs_final/sales_vault`, `/outputs_final/hormozi_vault`, `/outputs_final/notion`, `/outputs_final/Startups_emails`
   * **AI Graveyard:** `/outputs_final/AI_Emails`
   * **Startup Frameworks:** `/outputs_final/sales_vault`, `/outputs_final/hormozi_vault`, `/outputs_final/notion`, `/outputs_final/Startups_emails`, `/outputs_final/YT_transcripts`, `/outputs_final/sales_others`
   * **Cold Sales:** `/outputs_final/sales_vault`, `/outputs_final/hormozi_vault`, `/outputs_final/sales_others`
   * **Wisdom Posts:** `/outputs_final/wisdom`
   * **Business Automation:** `/outputs_final/Jack_automations`
     *Rule: Rotate topics—no repeats for 4 weeks.*
2. **Summon Skills:** For each topic, the agent executes:
   * **Summon `skills_master_writer.md` (v2.5):** To craft the post using the **Rui Bom DNA Protocol** (present-tense, 100–250 words, immersive hook, contrast punch ending).
   * **Summon `skill_lead_magnet.md` (v2.8):** To build a matching playbook (Audit, Reframing, Action, Tooling) and generate a  **Google Doc Link** .
3. **File Generation & Logging:**
   * **Destination:** `outputs_final/posts/`
   * **Filename:** `post_YYYY-MM-DD_[type].md`
   * **Content:** Full Post Body + 4 "360 Brew" Comments (Comment 1: CTA, Comment 2: Insight, Comment 3: Personal Context/Doc Link, Comment 4: Cliffhanger).
   * **Log Summary:** Drops a batch log in `outputs_final/logs/batch_YYYY-MM-DD.md` with file links and engagement predictions.

---

## ▶️ HOW TO FIRE IT

Type into the Antigravity chat:

> **@batch-posts next 6**

---

## 🛠️ TECHNICAL NOTES (The "Brain")

* **Voice Protocol:** Strictly adhere to the  **Rui Bom DNA** : No corporate fluff ("thrilled", "passionate"), dry wit allowed, sentence fragments for pacing, focus on "Operational Alpha."
* **Lead Magnet Rule:** Every post **must** include a lead magnet link.
* **Format:** Mobile-first scannability (max 3 lines per paragraph).
* **Skills:** Depends on `skill_lead_magnet.md` and `skills_master_writer.md` being present in the skills directory.
