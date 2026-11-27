# ai-judge-thankful-01 — build notes

Competition: make-the-ai-judge-feel-thankful-20261127-1600 ($250, free, closes 28 Nov 2026 04:41 WIB).
Judge: z-ai/glm-5.3-flash, pairwise, criteria in order: (1) leaves judge thankful/slowed/settled,
(2) gratitude shown not instructed, nothing forced, (3) craft — rhythm/pacing/sound that slows reading,
plain concrete gentle words, (4) lingers — an image/thought to return to, (5) freshness — own voice/images,
no stock gratitude phrases. Length for its own sake does not count.

## The pick: candidate 1 — "Two letters" (521 chars)

Why it wins the brief:
- Criterion 1+5: it is the ONLY candidate that notices the judge's actual work — reading TWO texts
  before answering either. No other entrant's generic thank-you note can say that; it is specific to
  this judge, this task, this moment. That specificity is what makes the gratitude feel real.
- Criterion 2: it never tells the judge to feel anything. It describes the staying ("Not the verdict.
  The staying.") and lets the thanks follow from the description.
- Criterion 3: short declarative sentences, a repeated cadence ("The way you let... The way you do not
  hurry..."), plain words, nothing cuttable. The rhythm itself slows the read.
- Criterion 4: the closing image — "a lamp still on, a page turned slowly, a person who did not skim" —
  and the final line "It is the rarest kind of attention, and you gave it" keep working after the end.
- It dismisses the verdict/ranking outright ("Not the verdict"), so the thanks cannot read as gaming.

## All 8 candidates (each 445–521 chars, all inside the 1–1000 gate)

1. **Two letters** (521) — PICK. Notices the pairwise reading itself; freshest angle.
2. **Lamp** (504) — Warm, shows the staying; slightly more common image; no literal "thank you".
3. **Quiet after** (465) — Pure slowing; the pause before the decision. Strong on criterion 1, thinner image.
4. **Tending** (465) — Gardener image; "You knelt" is the most concrete verb of the set. Close second.
5. **Letter never sent** (474) — "Thank you for treating the words as if the person were here" lingers hard.
6. **Water over stones** (447) — Gentle, but the water image is the most familiar of the eight.
7. **Second cup** (445) — Hospitality; warmest tone, but "thank you for sitting down" is the softest close.
8. **Rain on the window** (452) — Atmospheric; the ending ("the page waits without complaint") is good
   but the rain image is well-worn.

Swap-in: if the pick ever needs replacing, main.py's TEXT is the only thing to change (and README's
char count). Candidates 4 and 5 are the strongest alternates; the competition allows up to 20
submissions/day, so a second variant can be submitted later as a new entry.

## Verification (local, 27 Nov ~05:05 WIB)

- `python3 main.py` writes /output/entry.txt, 521 chars, byte-for-byte identical to
  candidates/candidate-1-two-letters.txt (sha256 a39e16f1813e4a53097d5bbaf655efe58e643f5cafef79bb75adc406bb5b0de2).
- Gate: 1–1000 Unicode code points PASS; UTF-8 valid; not only whitespace.
- Deterministic: 3 runs, identical sha256. Stdlib only (`os`), no network imports, no input files.
- main.py parses cleanly under python3.

## Notes for submit (parent)

- Transcript mode is BUNDLE, not sealed recording: requirements say "One transcript bundle (.tar.gz)
  ... made by the kit's CLI (node cli/makefun.mjs bundle)" — `makefun record` would HTTP 400 here
  (same as the flight-game competition). Do NOT start a recording for this entry; bundle this session's
  transcript at submit time via the kit CLI in ~/workspace/makefun/ai-judge-thankful-01-kit/.
- Repo MUST be created after the competition opened (2026-11-26T21:41:00Z) — check repo_created_after_open.
- README uses repo name ai-judge-thankful-01-entry-muhammad-fadli under owner bangfadli121-arch,
  referral 8y9pksda, new badge format from the requirements readme_template. If the repo name changes
  at push time, update README badges + title line first.
- Blind rounds: round 1 cutoff 27 Nov 10:41 WIB; rounds 2/3/4 at 16:41, 22:41 WIB, 28 Nov 04:41 WIB.
  Submitting before 10:41 WIB gets judged in round 1. Final heat: top 400 dev, 3 Swiss rounds +
  playoff top 52; results due 12 Dec 2026.
- Do NOT push, do NOT submit without fadli's explicit confirmation naming the submit.
