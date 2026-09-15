# Open issues — Who Makes History Happen? (review of Weeks 2–4, used in 5.1)

Production notes for the instructor. **Nothing here belongs on a slide.** Clear
an item and delete it.

Last reviewed: 2026-09-15, by a fresh-context review. Its findings were checked
against the sources and worked in. What was kept on purpose is listed below.
The Herodotus and Thucydides slides were added afterward at the instructor's
request. They were checked against their sources but not by a second
fresh-context review.

---

## 1. Sima Qian's English translator is not identified

**Status:** open.

The Xiang Yu verdict ("relied on his own intelligence without learning from the
past… was this not a great fallacy!") reuses the wording in
`greeks-evidence-and-purpose`, which doesn't name its translator either. The
meaning has been checked against the Chinese on ctext (*Shiji* 7, 太史公曰): 奮其私智而不師古
… 乃引「天亡我，非用兵之罪也」，豈不謬哉. The wording is faithful, but the translator is unknown.

**What to do:** identify the translation. Watson's *Records of the Grand
Historian* is the likely candidate, but that is a guess. Then add the
translator to the `.label` line and to the translations on the title slide.

## 2. The assigned Melian Dialogue translator is not identified

**Status:** open, low priority.

The assigned PDF (`melian-dialogue.pdf`, "A selection from The History of the
Peloponnesian War") is not Crawley. It gives 5.89 as "the strong do what they
can, and the weak submit," where Crawley has "the weak suffer what they must."
The deck quotes the assigned wording, because that is what students read, and
cites 1.22, 1.23 and 5.26 from Crawley (Gutenberg #7142). The title slide says
so ("Crawley; Melos from the assigned selection").

**What to do:** name the translator of the assigned selection. Note that
`greeks-evidence-and-purpose` quotes Crawley's wording of 5.89, not the
assigned one.

---

## Deliberate deviations — don't re-raise

**No `.image-notes` slides, and only images students have already seen.** Every
image is copied from an earlier deck. Each returning person gets the portrait
used before: Herodotus, Thucydides, Sima Qian, Machiavelli, Kant and Ranke.
Livy has no portrait in the earlier decks, so Botticelli's *Lucretia* follows
his slide. At the instructor's request, the review reinforces images students
already know and stays in period, instead of adding new pictures. An earlier
draft's four modern images were removed: a Gettysburg staff ride, a Moore's law
chart, the Kew reading room and NASA's earth at night. Don't add modern images
back. This is a short review placed in front of the Marx deck, not a full
session.

**The objectivity discussion has no answer slides, on purpose.** The five
discussion slides (break, holler out, partners, history applied, continued) are
rebuilt from the instructor's `1105r&vhdiscussion.pdf`. Their wording is kept
except for three edits: "does von Humboldt and Ranke" became "do Humboldt and
Ranke," to match the other decks; the capitals are gone; and the "What does it
look and sound like?" prompt was split into its own sentence. The exercise
comes after the recap and immediately before the closing "This week" slide,
which hands off to Marx. Its questions stay open, and the
closing slide picks them up: "Ranke's objectivity rests on what participants saw
and wrote down. What happens to it if the real cause is something none of them
saw?" The Marx deck is where that gets answered. Its prompts run longer than
SLIDE-STYLE's one-question norm because they are working instructions for
pairs, not a single question for the room.

**The discussion slides use their own colors.** They take the PDF's palette
(background #1c1c1c, white headings, orange #fc6736) so the exercise stands out
from the lecture. This is set by a small `<style>` block in `index.md`, just
above the discussion slides. It overrides the theme's `--ts-*` color variables
on `section.discussion-pdf` and sets `data-background-color` on each section.
It is deck-local, not part of `reveal-lecture-theme.css`. The fonts stay the
theme's; the PDF uses Archivo Black and Raleway Bold.

**Primary sources only.** At the instructor's request, nothing on the slides
quotes Popkin, Green and Troup, or any other secondary reading. Bede is
paraphrased, not quoted, to save space.

**Left out: al-Biruni, Voltaire, Carr (Week 1); Humboldt appears only in the
discussion prompts.** They were cut to keep
the review to one line of argument. The biggest omissions are al-Biruni's rules
of evidence and Voltaire's history of manners. Voltaire could go in as a reveal
on the Kant slide.

**Some quotations come from outside the assigned selections:**

- **Machiavelli ch. 25.** Schedule 3.2 assigns ch. 1–8. Ch. 25 is kept as the
  reveal, not the lead, because Fortune taking "one-half of our actions" is the
  cleanest statement of how Machiavelli divides causes. The assigned ch. 6 leads
  the slide.
- **Thucydides 1.22, 1.23 and 5.26.** Schedule 2.1 assigns the Funeral Oration
  and the Melian Dialogue. 1.23 leads the Thucydides slide because it is the
  earliest distinction in the course between the stated reason for a war and
  its "real cause." It is still the cause of one war, which the closing question
  uses. 1.22 is the passage students meet in Popkin. The assigned Melian
  Dialogue supplies the reveal.

**How Ranke is presented.** The headline "Kant hoped history had a plan. Ranke
said none could be proved" rests on the 1854 lecture. There Ranke calls both a
"general directing will" and "an onward-marching progression of the spirit
which necessarily drives it toward a defined goal" "neither philosophically
tenable nor historically provable." The same lecture allows "a certain sort of
progress," "absolute progress" in "material interest," and "great spiritual
tendencies" that dominate an epoch. So the deck doesn't say Ranke denied all
progress or all large-scale forces, only that no plan could be proved. An
earlier draft built the review on "every cause had a will." That was dropped
because Ranke's 1854 rejection of a directing will contradicts it, and
Thucydides' "growth of the power of Athens" strains it too.

**Livy's cause is "character, of a ruler or of a whole people."** Sima Qian's
verdict blames one man. Livy's preface explains Rome's decline collectively
("with the gradual relaxation of discipline, morals first gave way").

**Citation formats follow each text's own convention.** Bede is cited by book
and chapter in Roman numerals (I.7), as in `divine-power-and-statecraft`.
Herodotus and Thucydides are cited by book and section (1.1, 1.86–87, 1.23).

**The Herodotus 1.1 quotation starts mid-sentence** ("...that the memory of the
past"). The LacusCurtius transcription of Godley reads "in order that so the
memory," and the stray "so" is left out of the quotation, not silently
corrected.

**The *Manifesto* reads "society," not "societies."** The assigned PDF
(marxists.org transcription of the 1888 Moore translation) has "all hitherto
existing society"; Project Gutenberg #61 has "societies." The deck follows the
assigned reading, as `marx-structural-history` does.

**The schedule link is commented out**, matching the Marx deck's link in 5.1.
Uncomment both when the slides go live.

**Sources checked (2026-09-15):**

- Herodotus 1.1, 1.5 and 1.86–87 (Godley, LacusCurtius)
- Thucydides 1.22, 1.23 and 5.26 (Crawley, Gutenberg #7142); 5.89 (the assigned PDF)
- Livy, preface (Foster, the uark.edu text on the syllabus)
- Machiavelli ch. 6 and 25 (Marriott, Gutenberg #1232)
- Kant, Introduction (Beck, the Wikisource page on the syllabus)
- Ranke, 1824 and 1854 (GHDI document 358)
- *Anglo-Saxon Chronicle*, 793 (Giles, Wikisource)
- *Manifesto*, Part I (the assigned PDF)
- Engels, speech at the grave of Karl Marx, 17 March 1883 (marxists.org)
