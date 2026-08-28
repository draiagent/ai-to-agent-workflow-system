# 🤖 CLAUDE.md — AI Work Standards & Best Practices

> How to work effectively with Claude, ChatGPT, or any LLM using the ai-to-agent system

---

## 📌 Core Principle

**Structure beats conversation**

Instead of vague back-and-forth, give AI a clear, structured spec (VAC). Then let it execute.

---

## 🎯 How to Use This Document

### If you're a... | Start with...
**LLM User** | Section: "How to Prompt"
**Team Leader** | Section: "Implementing the System"
**Developer** | Section: "Integration Patterns"
**Beginner** | Section: "Simple Example"

---

## 💬 How to Prompt (The Right Way)

### ❌ Wrong Way (Vague)
```
"Can you help me make a marketing presentation?"
```

**Problem**: AI guesses what you want → Iterates 10+ times → Wastes time

---

### ✅ Right Way (Structured VAC)

```
Here's my workflow specification:

① GOAL
Create a product launch presentation that...

② INPUT
I'm providing:
- Product brief (attached)
- Target audience (CFOs, age 40+)
- Existing brand guidelines

③ ASSETS
- Logo files
- Case study data
- Pricing sheet

④ RULES
- Must be 12 slides
- Follow brand colors (blue+gold)
- Include ROI calculation
- Time: 2 weeks to launch

⑤ STEPS
1. Market positioning (Slide 1-2)
2. Problem/Solution (Slide 3-4)
...

⑥ TOOLS
- Use Claude Opus
- Format: PowerPoint (.pptx)
- Design: Professional corporate style

⑦ OUTPUT
PowerPoint file ready to present

⑧ ACCEPTANCE
✓ All 12 slides complete
✓ Design matches brand
✓ CFO approves before Friday
✓ Technically sound (no errors)
```

**Result**: AI understands exactly what you want → Executes once → Done

---

## 🔄 The Five-Step Workflow (With AI)

### Step 1: Create VAC (You)
Write your workflow spec using the VAC template.
**Time**: 15-30 minutes (first time), 5 minutes (repeat)

### Step 2: Give VAC to AI (You)
Paste your complete VAC into Claude/ChatGPT

**Prompt Template**:
```
[Paste your complete VAC]

Please execute this workflow specification.
Follow the RULES and STEPS exactly.
Deliver the OUTPUT in the requested format.
```

### Step 3: Execute (AI)
AI executes based on your spec.
**Time**: Depends on complexity

### Step 4: Verify (You)
Check result against ACCEPTANCE criteria.

**VERIFY Checklist**:
```
☐ Logic: Does it make sense?
☐ Flow: All steps complete?
☐ Visual: Looks right?
☐ Data: Numbers correct?
☐ Business: Meets GOAL?
```

### Step 5: Review & Learn (You)
Review from 6 perspectives, then store for reuse.

---

## 📋 VAC Template (Quick Reference)

```
## ① GOAL
[What's the end state?]

## ② INPUT
[What data/info do you need?]

## ③ ASSETS
[What resources exist?]

## ④ RULES
[What are the constraints?]

## ⑤ STEPS
[How to execute? (numbered with timeline)]

## ⑥ TOOLS
[What AI/tools to use?]

## ⑦ OUTPUT
[What's the deliverable?]

## ⑧ ACCEPTANCE
[Objective criteria for success]
```

---

## 🎯 Working with Different LLMs

### Claude Opus (High-Level Reasoning)
**Use for**: Complex, unknown tasks  
**Cost**: ¥50 per use  
**Best for**: First-time exploration, creating VACs

**Example Prompt**:
```
I need to design a completely new product launch strategy.
Here's what we know: [data]
Here's the constraint: [rules]
Please explore multiple approaches and recommend the best one.
```

---

### Claude Haiku (Fast Execution)
**Use for**: Known tasks, once VAC exists  
**Cost**: ¥5 per use  
**Best for**: Executing stored VACs

**Example Prompt**:
```
[Paste existing VAC]

This is a task we've done before (VAC v1.0).
Please execute using the stored specification.
```

---

### GPT-4 / Gemini (Comparison)
**Works the same way**. Just adjust model names in VAC TOOLS section.

---

## 🚀 Prompt Template for Execution

Use this when giving AI a VAC to execute:

```
TASK: Execute the following workflow

SPECIFICATION:
[Paste entire VAC]

INSTRUCTIONS:
1. Follow the STEPS in order
2. Respect all RULES
3. Deliver exactly as specified in OUTPUT
4. Format should match the example

QUALITY CHECK:
Before delivering, verify against ACCEPTANCE criteria:
- [ ] [Acceptance criterion 1]
- [ ] [Acceptance criterion 2]
...

If any criterion isn't met, flag it and explain why.
```

---

## ⚠️ Common Mistakes & Fixes

### Mistake 1: Over-Prompting
```
❌ "Can you create a marketing plan? 
    Make it creative. 
    Include social media. 
    Make it engaging. 
    Should work for startups.
    Think about budget..."

✅ Use VAC template instead
```

### Mistake 2: Under-Specifying
```
❌ "Make a presentation"

✅ "Create 12-slide product launch presentation,
    PowerPoint format, brand guidelines attached,
    for CFO audience, ready by Friday"
```

### Mistake 3: Iterating Without Structure
```
❌ "The colors are wrong. Make them different. 
    Actually, the layout is off. 
    Can you also add more data?"

✅ Save all feedback into VAC v1.1
   Then re-execute with updated VAC
```

### Mistake 4: Not Verifying
```
❌ "AI said it's done, so it's done"

✅ Run through VERIFY checklist
   Check: Logic, Flow, Visual, Data, Business
```

---

## 📊 Choosing the Right Model by Task

| Task Type | Model | Cost | Reason |
|-----------|-------|------|--------|
| Explore new problem | Opus/GPT-4 | ¥50 | Complex reasoning needed |
| Write from template | Haiku/GPT Mini | ¥5 | Clear spec exists |
| Simple execution | Haiku | ¥5 | Routine task |
| Auto-delegate | Agent | ¥0.5 | Fully automated |

---

## 💡 Pro Tips

### Tip 1: Version Your VAC
```
VAC-001-v1.0-product-launch.md (first version)
VAC-001-v1.1-product-launch.md (improved version)
VAC-001-v2.0-product-launch.md (major revision)
```

### Tip 2: Store Successful VACs
Once a task works, save the VAC forever.
Next similar task: Copy VAC, change 10%, execute in 30 seconds.

### Tip 3: Create Skill Templates
```
SKILL-001-v1.0-short-video-script.md
(Reusable for all short video projects)
```

### Tip 4: Use Multi-Model Routing
```
Task arrives
  ↓
Is it in our VAC library?
  ├─ YES: Use Haiku (¥5, 30 sec)
  ├─ NO: Use Opus (¥50, explore)
  └─ Once solved: Store for next time
```

---

## 🔄 Continuous Improvement Loop

```
Execute with VAC-v1.0
        ↓
Verify & Review
        ↓
Identify improvements
        ↓
Create VAC-v1.1 (same structure, better details)
        ↓
Next similar task uses VAC-v1.1
        ↓
Better results, lower cost, faster execution
```

---

## 🎓 Example: Complete Workflow

### Scenario: Create Short Video Script

**Step 1: Create VAC (15 min)**
```
① GOAL: 60-second short video script on blood glucose management

② INPUT: 
- Target audience: Health-conscious millennials
- Tone: Educational but accessible
- Platform: TikTok/Instagram Reels

③ ASSETS:
- Existing video templates (3 options)
- Brand voiceover guide
- Caption style guide

④ RULES:
- Max 60 seconds (translates to ~150 words)
- Must include hook, explanation, CTA
- Use 2-3 visual transitions

⑤ STEPS:
1. Write hook (first 5 sec) - attention-grabbing fact
2. Explain concept (40 sec) - clear breakdown
3. Add CTA (15 sec) - what to do next

⑥ TOOLS: Claude Haiku (script creation)

⑦ OUTPUT: Script in markdown format, timestamped

⑧ ACCEPTANCE:
✓ Exactly 60 seconds (verified timing)
✓ Hook engages immediately
✓ Explanation clear for average viewer
✓ CTA specific and actionable
```

**Step 2: Give to Claude (2 min)**
```
[Paste entire VAC above]

Please execute this workflow and deliver 
the video script in the specified format.
```

**Step 3: Verify Result (5 min)**
```
Logic: ✓ Facts correct
Flow: ✓ Hook-Explain-CTA structure clear
Visual: ✓ Reads well
Data: ✓ Timing checks out (count words)
Business: ✓ Meets all success criteria
```

**Step 4: Review (5 min)**
```
Scope: ✓ Created exactly what was asked
Complexity: ✓ Not over-engineered
Security: ✓ No personal data exposed
Edge Cases: ✓ Works for different viewers
Consistency: ✓ Matches brand voice
Regressions: ✓ Doesn't conflict with other scripts
```

**Step 5: Store (5 min)**
```
Save as: VAC-045-v1.0-short-video-60sec.md
Location: Knowledge base → Short Video → Scripts
Next use: Copy this VAC, change topic, execute with Haiku
```

**Total Time**: 30 minutes (first time)  
**Next Similar Video**: 30 seconds (copy VAC, change topic, execute)

---

## 🚀 Enterprise Implementation

### For Team Leaders

**To implement this system in your team**:

1. **Week 1**: Introduce VAC concept
2. **Week 2**: Everyone creates their first VAC
3. **Week 3**: Build VAC library together
4. **Week 4+**: Use library for rapid execution

### Expected Outcomes
- Communications failures: ↓ 80%
- Rework: ↓ 40%
- Time to completion: ↓ 60%
- Team satisfaction: ↑ 40%

---

## 📞 When to Use This System

✅ **Use this for**:
- Repetitive tasks (happens 2+ times)
- Complex outputs (writing, design, analysis)
- Team collaboration (multiple people)
- Quality control (mistakes are costly)
- Knowledge preservation (learning from success)

❌ **Skip this for**:
- One-time simple questions
- Instant feedback ("What's the capital of France?")
- Real-time conversation

---

## 🎯 Success Metrics

Track your VAC usage:

| Metric | Track | Target |
|--------|-------|--------|
| VACs Created | Count | 10+ per month |
| Time Saved | Hours | 80% reduction by 10th task |
| Cost Per Task | ¥ | ¥50 → ¥0.5 |
| Knowledge Reuse | % | 80% by month 3 |
| Team Adoption | % | 70% using system |

---

## 📚 Additional Resources

- Full system: [README.md](./README.md)
- Templates: [/templates](./templates/)
- Examples: [/case-studies](./case-studies/)
- FAQ: [/faq](./faq/)

---

**Version**: 1.0 | **Last Updated**: Aug 2026 | **Maintainer**: AI Coach (@draiagent)

```
╔═══════════════════════════════════════════════════════════╗
║  Structure beats conversation                             ║
║  VAC once, execute forever                                ║
║  — ai-to-agent workflow system                            ║
╚═══════════════════════════════════════════════════════════╝
```
