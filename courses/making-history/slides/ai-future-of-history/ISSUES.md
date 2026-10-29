# Open issues — AI and the Future of History (11.2)

Contributor notes, excluded from the build. Deliberate deviations are recorded
here so a later review does not raise them again.

## The slide contract this deck is built on

**The brief (2026-10-27).** Prepare a lecture on how AI could change archiving,
historical narrative and historical practice, in the course's terms. It opens
with how a language model works, since most students don't know. It then shows
how a model reflects bias, does not understand, and yet produces compelling
narratives, and what that means for historical practice. The author also asked
for "a more modern, AI aesthetic" distinct from the course's usual decks; see
"The machine theme" below.

The session has no reading. The students' Campus History AI essays are due the
same day. The deck has no discussion slides; see "Discussion slides removed"
under Decisions.

**Four parts, by question rather than by source.** The guide's default is one
part per source or person. This session has no assigned source, so each part
takes one question and reads it against a historian the class already knows.
The headlines read in order as one argument:

1. **How a chatbot works.** A model is trained to predict the next piece of
   text. Three diagrams show the mechanism: tokens, a probability list, and
   three sampled runs. A search-enabled chatbot differs from one that works
   from memory. Tuning is done by about forty hired raters (Ouyang et al.).
   A reasoning model's notes and answer follow, then Chen et al. on why the
   notes are not a record of how the answer was reached.
2. **Whose text.** Carr's facts that speak "only when the historian calls on
   them" (p. 11): in a model, frequency decides instead. The pronoun diagram
   follows. Then the Stochastic Parrots paper, its authors' portraits, and
   their claim that every step favors the dominant view (p. 614). Trouillot's
   four moments (p. 26), the 1791 diagram, and the training pipeline mapped
   onto his moments.
3. **Fluent without meaning.** The stochastic parrot (pp. 616–17), and the
   coherence the reader supplies (p. 616). Gurnee and Tegmark are the
   counterweight: a model does learn a rough map of the world, but they
   tested it only on well-known places (p. 13). The three
   invented dissertations and why training rewards a bluff (Kalai et al.).
   Maza's embargo on invention (p. 225).
4. **The record.** Machine learning reads the Herculaneum scrolls; a quote
   slide gives what PHerc. Paris 4 says and what a historian gains from it.
   Generated text ended the wordfreq project. Carr's "study the historian"
   (p. 23) still holds, but a chatbot has many authors. Four cards on what
   changes for practice.

The close follows: the arc, the take home, then "What is Zimmerman Library?"
and two photographs of it, 2010 and 1938, captioned with their metadata only.
The author uses them to make the point that "what is X" always has a
chronological dimension. A pointer to the archive session ends the deck.

**Test any new slide by reading the headlines aloud in order.** If it does not
read as the next sentence, it belongs somewhere else or nowhere.

**The cold open is the Turk.** It uses Racknitz's 1789 plates I and III as
bleeds. The question slide follows, then an image-notes slide that works the
pair, ending on Amazon's Mechanical Turk. The question it plants, "Where is the
person in a machine that writes?", is answered by parts two and four: the
writers in the training data, the raters, and the reader who supplies the
coherence.

**The model data is real.** Every probability on the five probability diagrams was
measured for this deck on two small open models, GPT-2 (2019) and OLMo 2 1B (2025).
The reasoning diagram is one recorded run of a third, Qwen3 1.7B (2025). The
method is in `images/README.md`, "The diagrams". The deck draws three
conclusions from them:

- Both models complete "In 1791, a great revolution began in" with France. The
  2025 model gives Haiti only for a slave-revolt prompt (35%), so it files
  Haiti under revolt, not revolution. That is Trouillot's "unthinkable" made
  measurable.
- "He" leads after "The historian said that" in both models, and "she" leads
  after "The nurse said that".
- The 2025 model's first sampled run gives a near-correct date (1936) with an
  invented claim ("the first modern library to be built in the United
  States").
- Asked when Zimmerman was built, the reasoning model's notes say "I should
  verify this" and "Let me confirm once more" without looking anything up.
  It answers 1952, designed by "H. H. Richardson & Company". Five runs gave
  five wrong dates: 1952, 1939, 1934, 1961 and 1923.

These are small models, not the tuned commercial chatbots the students used.
The citation note on the title slide says which models were run, and the
captions name the model on every diagram.

## The machine theme

**`theme: machine` in the front matter** loads `assets/css/reveal-lecture-machine.css`
and Space Grotesk after the base theme. The `reveal-lecture` layout does this,
so every class keeps its markup and only its look changes. The file's header
comment maps the slide levels to their new faces:

- labels: cyan mono;
- claims: Space Grotesk in solid violet (`#a78bfa`). A cyan-to-violet gradient
  was the first version; the author found it too much (2026-10-29);
- sources: Fraunces italic in amber and rose, kept warm and serif on purpose,
  so the human writing quoted on the slides stands apart from the deck's own
  voice;
- questions, commentary and apparatus: unchanged.

The short divider under each headline is hidden (`display: none` on `hr` and
`.rule`). The author asked for it gone on 2026-10-29. Decks still write
`---`, so the markup matches the guide and the base theme keeps its rule.

The background is a dark page with two faint glows and a dot grid. The title
headline has a blinking caret.

**Headlines are in sentence case, not reveal's capitals.** This departs from
every other deck in the course. The theme sets `text-transform: none` on
`.main-point` and on card and step headings. The long claim headlines read
faster that way, and the capitals belong to the course's usual look. This is
the author's call. To restore capitals, delete the two `text-transform: none`
lines in the theme file.

**Image slides carry no `data-background`.** The page background shows behind
the picture. Bleed slides set `data-background-color="#07080d"` to match.

The theme is not yet described in `SLIDE-STYLE.md`. If it is kept, it belongs
there as an option, with the rule that it changes faces and colors, never
levels.

## Decisions

**Throughline aligned with the neighboring decks (2026-10-27).** The 9.1 and
11.1 decks show the two sessions just before "now". In their throughlines,
10.2 (Campus history with AI) already carries the line "A machine that puts
words together the way readers expect". This deck's past nodes are therefore
10.2 and 11.1, each in its own deck's words. The 11.2 node is new:
"Probability. A chatbot's history follows what was written down most often."
It matches the take home.

The 11.1 deck's "next" node had said "AI and campus history: the campus as a
landscape with a past, and the archive behind it". It now carries the same
11.2 line, so the forward reference is accurate. The 12.1 node is written from
`schedule.md`, because no 1619 deck exists yet.

**Introduce before you quote: an open question for the author.** The guide's
only exemptions are the narrator (a `Background:` reading) and voices quoted
through the narrator. This session has no reading, so neither applies. The
guide has no rule for a deck that brings back authors from earlier weeks.

- Bender and Gebru have the paper, then both portraits, before their first
  words.
- Carr (p. 11, p. 23), Trouillot and Maza are course authors read in earlier
  weeks, with their own decks. Each eyebrow names the author and year or week.
  Maza cannot have a portrait (the author's rule, 2026-10-11: no photographs
  of textbook authors; see `inventing-nations/ISSUES.md`). No free portrait of
  Trouillot turned up. Carr's own deck (1.2, an older HTML deck) has no portrait.
  The deck treats all three as already introduced, the way a review deck
  does.
- Ouyang et al., Kalai et al. and Gurnee and Tegmark are quoted as documents
  by institutional teams, with OpenAI or MIT in the eyebrow and the paper in
  the cite.
- Robyn Speer is quoted once, as the maintainer of wordfreq. The headline
  introduces the project before the quotation, and the cite names her.
- `deck-check.sh` checks the before-intro rule only against portrait surnames,
  and passes.

**Explainers.** The Trouillot explainer has a figure and a quotation but no
`.detail` lines; the quotation is the explanation. The Gurnee and Tegmark
explainer has one `.detail` line, saying what their test included and that
"understanding" is still argued over.

**Part openers.** The guide asks each part to open with a `.detail` line saying
what the last part left unfinished. Here only part four does: its opener has
no quotation and needs the bridge. Parts two and three open on quote slides
whose headlines do the bridging: "In a language model, frequency decides which
facts get the floor" and "Bender, Gebru and their coauthors call a language
model a stochastic parrot". A `.detail` line under a quotation would put commentary in a
hierarchy with evidence.

**The 1791 diagram follows the Trouillot explainer** rather than preceding it,
so the class has his four moments and the "unthinkable" before seeing the
models fail it.

**The ChatGPT sentence is a paraphrase.** The historical block on the raters
slide says ChatGPT was trained the same way as InstructGPT "by OpenAI's own
account". The source is OpenAI's announcement "Introducing ChatGPT" (30
November 2022). That page returned 403 to the command line, so the wording
could not be checked against it and stays outside quotation marks. A later
pass with a browser could quote it.

**Gebru's departure is given both ways.** Google said she resigned; she says
she was fired over this paper. The caption says both.

**Voice fixes after the first full read (2026-10-27).** Five headlines and
lines were rewritten:

- A coined metaphor ("clouds others") became a plain claim ("pollutes others").
- A numeric-pairing epigram ("three chatbots invented three") became a
  sentence.
- The practice-cards headline promised a "what does not change" the cards
  never delivered.
- The take home's two-claim "and" sentence lost its second claim.
- The Herculaneum caption had the models "reading" the Greek. People read it;
  the models made it legible.

**Next-token caption (2026-10-27).** It had compared GPT-2's token rank for
1889 ("third", behind the half-year " 18" and " 17") with OLMo's whole-year
rank (23rd). It now compares like with like: as whole years, 1889 is GPT-2's
top choice. The alt text had said the chart shows two models; it shows GPT-2
only.

**Two reasoning slides (2026-10-28), at the author's request.** They follow
the raters slide, not the search slide as first proposed. Reasoning is trained
on top of the tuning the raters slide describes, so it reads as the next stage.

- *An image slide* shows one run of Qwen3 1.7B in thinking mode. The caption
  says the notes "speak of checking, yet nothing was looked up". That is
  literally true: the run had no search or tools. The caption also says
  reasoning "is trained on questions with a checkable answer: math, not
  history". That describes the teacher models; Qwen3 1.7B was distilled from
  them. See `images/README.md`, "The reasoning diagram", for the method and
  the four other runs.
- *A quote slide*: Chen et al. (Anthropic, 2025), p. 7, checked word for word
  against the rendered page. The 25 and 39 percent figures are the overall
  faithfulness scores on p. 6. Anthropic makes Claude, one of the two models
  tested, so this is a company reporting a weakness in its own product, as
  Ouyang et al. do for OpenAI. The cite uses the short form, without
  "(Anthropic, 2025)", because the eyebrow carries it and the long form
  overflowed the slide by 12 px.
- The title slide's source list and citation note now name Chen et al. and
  Qwen3.

**The three-runs diagram cannot be reproduced exactly (2026-10-28).** Running
OLMo 2 1B himself, the author got accurate answers for the Zimmerman prompt.
Samples vary with the model variant (base, not `-Instruct`), the prompt
wording, the sampling settings, and even the torch version and hardware. The
diagram records three draws, one of which (1936) is nearly right. A
reproducible alternative was offered: score each year's probability after the
prompt, as `years.py` does for UNM's founding. That awaits the author's
answer.

**Gurnee and Tegmark's point made explicit (2026-10-29).** The author asked
what the slide was for: learning, or bias? It argues both now. The headline
says a model holds more than a parrot's statistics. The quote, from p. 1,
gives their debate in their words; the author trimmed it to open at "…an
enormous collection", still verbatim. The `.detail` gives the catch from their
methods (p. 13). Their map uses only places with 5,000 Wikipedia page views,
"a proxy for whether we should expect an LLM to know of this place or not".
The detail paraphrases that, because the guide keeps quotations out of
`.detail`. Their timeline used "the 350 most famous people who died from each
decade", and they note their data "is skewed towards the Anglosphere", both on
p. 13. Neither fits on the slide, but both are good to say aloud.

**What the Vesuvius scroll says (2026-10-29), at the author's request.** It is
a quote slide after the Herculaneum image. The quotation, the rivals' "nothing
to say about pleasure", Xenophantus, "very likely" Philodemus (Richard
Janko's words), Philodemus as the villa's resident philosopher, and the 5
percent figure are all on the Vesuvius Challenge's Grand Prize page (5
February 2024), checked word for word on 2026-10-29. "Unseen for 2,000 years"
and "never-before-seen text" are the page's words. "Almost every other ancient
text decays" is from the scrollprize.org home page. The quotation opens
lowercase in the source, hence the ellipsis.

**The close rebuilt around one question (2026-10-29), at the author's
request.** One Zimmerman slide became three: the question, the 2010
photograph, and a 1938 photograph from the UNM Archives. The captions are
metadata only, by design. The old caption's list of the models' dates is gone
from the close; the dates remain on the three-runs and reasoning diagrams. The
1938 scan is the archive's only copy, at 794×530. It shows at 1.00×, so
deck-check warns.

**Discussion slides removed (2026-10-29), at the author's request.** Each
part had ended on a discussion slide tied to the students' essays: where your
dates came from, whose silences a chatbot inherits, the most convincing
sentence in your essay, and a history of this semester written in 2075. The
author removed all four because "we have discussion throughout all the
slides". The guide's discussion-slide type stays available. Don't argue them
back in.

**Reveals run top to bottom (2026-10-29), at the author's request.** Two
Compare blocks, Week 10.1 on the coherence slide and the AI essay guide on the
Kalai "why" slide, showed from the start, beneath fragments that appeared
later. Each is now fragment 2, after the unpack block. On the Kalai cards slide,
the table cite moved up under the cards, above the "The right answer" fragment,
so nothing static sits below a fragment. An audit of every slide found no other
block that is static under a fragment, no decreasing index, and no mix of
indexed and unindexed fragments. Screenshots of each fragment step confirm the
order in the browser.

## Open questions

- **Trouillot cover resolution.** 325×475 is shown at 262×382, which is 1.24×
  against the 1.5× target. `deck-check.sh` WARNs on it. Nothing larger turned
  up on Open Library, Commons or the publisher's pages; see `images/README.md`.
- **Vesuvius licence.** Commons says CC BY-SA 4.0 and the Vesuvius Challenge
  site says CC BY-NC 4.0. The caption carries the stricter licence.
- **Fair use.** The Trouillot cover and the Gurnee and Tegmark figure; the
  reasoning is in `images/README.md`.
- **Two captions run over the 40-word target:** next-token and the paper,
  both at 41 words. Both are under the 55-word stop, and each carries a model
  credit or licence that can't be cut.
- **OLMo's rank for 1889 (23rd)** was printed by `years.py` from the full
  1850–1960 scoring. The probe output was lost when the temporary
  scratchpad was emptied on 2026-10-28, so a rerun is needed to see any of
  the numbers again. The scripts survive in `_diagram-scripts/`; see
  `images/README.md`.
- **A careful-user test, run but not yet on a slide (2026-10-29).** The
  author asked how much hallucination is user error. Qwen3 1.7B, with the
  reasoning diagram's settings and seeds 1105–1109, answered the Zimmerman
  question three ways. Bare, it gave 1952, 1939, 1934, 1961 and 1923. With a
  system rule to say "I don't know" rather than guess, it gave 1920, 1964,
  1965, 1955 and 1965, never hedged, and twice invented the namesake. With
  the Wikipedia lead paragraph supplied and a request to quote it, it
  answered 1936–38 all five times. Each quotation matched the passage word for
  word, apart from capitalization and a final period. Script and output:
  `_diagram-scripts/reason_skill.py`, `reason-skill-Qwen3-1.7B.json`. Whether
  it becomes a slide awaits the author.
- **Sentence case** (see "The machine theme").
- **Introduce before you quote** for authors from earlier weeks (see
  Decisions). If the author wants a rule, it belongs in `SLIDE-STYLE.md`.
- **A talking point the 1791 slide leaves unsaid.** The French Revolution
  began in 1789, so "France" is wrong for the prompt too. The models reach for
  the famous revolution even when the date doesn't fit.

## What the fresh-context review caught (2026-10-27)

It found no misquotations. Every quotation matched its source word for word
at the cited page: Ouyang pp. 2 and 7; Bender et al. pp. 613, 614, 616 and
616–17; Trouillot pp. 26 and 29; Carr pp. 11 and 23; Maza p. 225; Kalai pp. 2
and 4; Gurnee and Tegmark p. 1; Speer; and the essay guide. It also confirmed
every model number against the probe files.

Each finding below was checked against the sources before it was fixed.

- **Three-runs slide.** The caption and alt text said three runs from one
  model; the diagram shows three from each of two. Now "One prompt, three runs
  from each model, six dates".
- **Throughline.** The reviewer read the deck before the realignment recorded
  under Decisions, which already fixed it.
- **"For eighty-four years, audiences paid…"** The Turk existed from 1770 to
  1854, but it was dormant for long stretches and debuted at court. Now
  "From 1770 to 1854 the Turk played chess before courts and paying crowds."
- **Tokens caption.** "Common words and even years are a single token" holds
  only for GPT-2; the diagram's own footnote says OLMo splits years. Now "In
  GPT-2, common words and many years are a single token."
- **1791 caption.** It credited "August 1791" to p. 27, which supports only
  "unthinkable", and called the colony Haiti. Now "Trouillot's 'unthinkable'
  revolution (p. 27) began in Saint-Domingue, now Haiti, in August 1791."
- **Take home and Maza block against the search slide.** "Cannot say where a
  sentence came from" contradicted a searching chatbot's real citations. Both
  now say what holds either way: nothing in a model separates sourced
  sentences from invented ones.
- **Carr p. 11 block.** "Nobody decides" negated the headline's verb and
  ignored the filters and raters. Now "No historian decides."
- **Part four: image models against language models.** The Herculaneum
  reading used vision models on CT scans, not a language model. Arc card 04
  now says "Image models read lost texts; language models fill the web…".
  The part opener already said "Machine learning".
- **Editions.** The citation note now names the Penguin Carr, the Beacon
  Trouillot (1995; the course PDF's filename says 2015, but its pages match
  the 1995 printing) and the Chicago Maza.
- **Kalai cards slide.** The `p.cite` held a sentence of commentary and a
  quotation. The commentary is now an `.unpack` block in paraphrase, and the
  cite is only the source.
- **Judgment calls taken.**
  - All four Parrots authors are credited: "Bender, Gebru and their
    coauthors" in the headline, and "Bender et al." in eyebrows and arc
    labels.
  - The Kalai eyebrows say "Kalai et al.", not "OpenAI", since Vempala is at
    Georgia Tech. The title slide names Ouyang et al. and Kalai et al.
  - The wordfreq headline is now "…stopped updating, saying generated text
    had polluted its data". Speer gives three reasons, and the headline no
    longer implies one. The practice card says "Since about 2021", matching
    her "post-2021".
  - "About ten times larger" is now "twelve times" (1.485B ÷ 124M).
  - The Gurnee caption and alt text say the points were read out by a
    trained probe, not "from internal activity alone".
  - Pipeline step 04 is now "What sticks": readers repeat the answer as the
    history, closer to Trouillot's retrospective significance than a bare
    feedback loop.
  - Racknitz's title is translated at first showing.
  - "The full method was printed only in 1857" acknowledges the partial
    1834 exposé.
  - Mechanical Turk is in the past tense.
- **Kept.**
  - The cold-open question slide's first bullet is a statement before the
    question. That is the model deck's shape (`annales-longue-duree`).
  - The `.parallel` on the search slide compares two modes, not two writers.
    The guide offers `.parallel` for non-writer comparisons under "Skip
    orientation furniture".
  - The `.flow` slides follow a sequence.
  - Zimmerman Library sits after the take home as the bridge to the closing
    slide, which points to the archive housed in it.
  - The take home answers the opening's "is it history"; "whose knowledge is
    in it" is answered on the Carr p. 23 slide and in arc card 02.

## Sources for review

- Emily M. Bender, Timnit Gebru, Angelina McMillan-Major and Shmargaret
  Shmitchell, "On the Dangers of Stochastic Parrots: Can Language Models Be Too
  Big?" *FAccT '21*, 610–623, doi:10.1145/3442188.3445922. Open access, CC BY
  4.0.
- Long Ouyang et al., "Training Language Models to Follow Instructions with
  Human Feedback," arXiv 2203.02155 (2022).
- Adam Tauman Kalai, Ofir Nachum, Santosh S. Vempala and Edwin Zhang, "Why
  Language Models Hallucinate," arXiv 2509.04664 (2025).
- Wes Gurnee and Max Tegmark, "Language Models Represent Space and Time,"
  ICLR 2024, arXiv 2310.02207.
- Robyn Speer, "Why wordfreq will not be updated," `SUNSET.md` in the wordfreq
  repository (September 2024).
- Vesuvius Challenge, "2023 Grand Prize awarded" (scrollprize.org, 5 February
  2024).
- E. H. Carr, *What Is History?* (1961), ch. 1: in the course folder.
- Michel-Rolph Trouillot, *Silencing the Past* (1995), ch. 1: in the course
  folder.
- Sarah Maza, *Thinking About History* (2017), ch. 6: in the course folder,
  with OCR in `.research-packets/`.
- Yanda Chen et al., "Reasoning Models Don't Always Say What They Think,"
  arXiv 2505.05410 (Anthropic, 2025).
- DeepSeek-AI, "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via
  Reinforcement Learning," arXiv 2501.12948 (v2, January 2026).
- Qwen Team, "Qwen3 Technical Report," arXiv 2505.09388 (2025).
- The course's Campus History AI essay guide, `../../campus-history-ai.md`.
- UNM Center for Southwest Research, "Library - Zimmerman - exterior - east
  side prior to additions," ULPhotoImag item 3086 (UNMA 028, box 66).
- Wikipedia, "Zimmerman Library," lead paragraph (fetched 2026-10-29): the
  passage supplied in the careful-user test.
