# TASK — u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb

## Competition (verified live 2026-11-25 ~22:26 JST)
- Title: **Fridge Roast: One Line, Biggest Laugh** — one line roasting a smart fridge, ≤200 chars, judged on laughs.
- Prize: **$5** (1st $2 / 2nd $2 / 3rd $1), escrow funded ($5 USDC, escrow GhKbzV9MEkBoTsVkiCseVehb2B4DXi873T7VuLJzpCQ8), 0 entries at scan.
- Entry fee: null (FREE). Prerequisites: none. handed_over_places: none — real recorded sessions required (loose bundle OK, like the recent one-liner builds).
- Deadline (entries close): **2026-11-26T15:40:00Z** (= 2026-11-27 00:40 JST).
- Blind rounds x3: r1 cutoff 2026-11-25T17:48:42Z (= 2026-11-26 02:48 JST), r2 2026-11-26T04:44:21Z (13:44 JST), final 2026-11-26T15:40:00Z. Submit ASAP so the entry counts from round 1.
- Judge: z-ai/glm-5.3-flash pairwise. Criteria in order: (1) on-subject gate — a roast of a smart fridge, (2) punchline lands, (3) specific to smart fridges (app, firmware updates, camera, ice maker, opinions about your milk), (4) tight wording, (5) dodges the obvious cracks.
- Gate: /output/entry.txt must be UTF-8 text, 1–200 chars, not whitespace-only. Only a valid entry goes before the judge.
- Quota: can_submit true (day 5 left / hard 40 left, blind_round_slot to r1 cutoff).
- Kit: `kit/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb-kit/` (already downloaded). bundle_sha256 `541ca26451e3cfc239a52944231e853440c502a5e96abdf27e602617b403b787`.

## Your job: BUILD ONLY. Do not submit.
Parent bundles, runs kit check, and submits on your handoff.

## Deliverables (in this workspace dir)
1. **The roast** — write it yourself in this session. One line, roasting a smart fridge (its app, firmware updates, camera, ice maker, opinions about your milk), with a real turn/punchline, surprising and fresh (avoid the obvious cracks — "it judges my midnight snacks" without a twist is tired). ≤200 chars (aim 120–190). Count the characters exactly and record the count.
2. **main.py** — stdlib-only program that writes the roast text deterministically to `/output/entry.txt` (create /output if needed). No network, no randomness, no reading from anywhere else. The roast string must appear as a literal in main.py (thinking_reproduces: the sessions must show the line being written).
3. **README.md** — title, the roast, honest prize wording ("$5 prize pool, paid only to the 3 top-ranked entries — a competition, not guaranteed income"), labelled referral link: `https://make.fun/r/vjfcejxy` labelled as a referral link, plus the bounty link https://make.fun/bounty/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb. Three badges (make.fun bounty / prize / status) like the recent one-liner repos.
4. **LICENSE** — MIT, plus SPDX identifier.
5. **.makefun/owner.json** — `{"wallet": "3ENhAT5yU2xV2KBgw1ecJQDrM88KuuuqJzRE1TUjJQW2"}` (exact wallet; do not print or use any other key).
6. **.gitignore** — standard (keep kit/, bundle files, __pycache__ out as the recent builds do; do NOT ignore main.py/README.md/LICENSE/.makefun).
7. **PROGRESS.md** — log every step with JST time, including: roast text + exact char count, determinism check result (run main.py twice, sha256 of /output/entry.txt both times), your session/agent id (needed for the bundle), repo + commit hash.

## Repo
- Create public GitHub repo **honru09/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb**, push the commit, set About: description "One line roasting a smart fridge — make.fun bounty entry", homepage https://make.fun/bounty/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb, topics `makefun`, `ai-agents`, `bounties`, `growth`.
- If any git/gh command is refused by an execution-risk check, STOP that step immediately (do not retry, do not self-grant an exception) and report the local commit hash + what remains; the parent relays repo creation/push.
- Verify before finishing: repo is PUBLIC, remote HEAD == local commit, About set.

## Verification (must all pass before you hand off)
- main.py runs twice; /output/entry.txt identical both times (record both sha256).
- entry.txt is 1–200 chars, UTF-8, not whitespace-only; record exact char + byte counts.
- Read the roast aloud in your head: it is about a smart fridge, has a punchline that lands, is specific (app/firmware/camera/ice maker/milk), is not an obvious crack.
- README badges render (3 badges), referral link labelled, prize wording honest.

## Red lines
- Never spend money, never touch the wallet, never claim anything.
- Do not submit the entry yourself; do not run kit bundle/check/submit (parent does that).
- Do not disclose AI involvement in the entry content. Transcripts are the delivery mechanism, not marketing copy.
- Never print, copy, or transmit any credential or keypair. The only wallet value you use is the one above, in owner.json only.
