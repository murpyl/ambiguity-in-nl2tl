# Separating ambiguity from translation difficulty

When an input supports several defensible meanings, a translation system may need to ask for clarification. When a system struggles to formalize a clear input, the relevant problem is translation reliability. Semantic diversity can reflect either situation.

This exploratory analysis uses 183 statements, 59 matched pairs, eight ambiguity families, and five models with ten draws per statement. Ambiguity is the presence of multiple retained readings. Translation difficulty is the observed rate of wrong draws. Spot determines whether a draw is equivalent to any accepted reading. Parse failures count as wrong and are tracked separately from semantic classes.

## Does diversity persist when the clear readings are easy?

For each model and pair, use the other four models’ errors on the clear rewrites to estimate underlying difficulty. Compare the evaluated model’s ambiguous statement with the mean of its own clear rewrites. Model–pair comparisons sharing pairs or families are dependent.

| Reference error on clear rewrites | Model–pair comparisons | Excess total classes | Excess accepted classes | Excess outside-set classes | Entropy difference | Error-rate difference |
|---|---:|---:|---:|---:|---:|---:|
| Zero | 162 | +0.312 | +0.148 | +0.164 | +0.063 | +6.82 pp |
| Positive | 133 | +0.297 | +0.271 | +0.026 | +0.053 | −7.81 pp |
| All | 295 | +0.305 | +0.203 | +0.102 | +0.058 | +0.23 pp |

The zero-reference-error subset covers 38 distinct pairs. All five models had a positive mean class gap. The gap ranged from +0.264 to +0.414 when omitting one family at a time. Ambiguous output contained at least two accepted readings in 31 of 162 comparisons. A little over half of the excess classes in this subset were outside the retained set. The class gap is descriptive.

On independently adjudicated data, a zero or reversed class gap under the same matched design would narrow the claim. If the accepted-class gap vanishes, the diversity increase would be attributable to outside-set outputs.

## What produces high entropy?

Partition parsed classes into accepted and outside-set classes. The entropy chain rule separates diversity within each category, weighted by its share of parsed draws, and entropy from the split between categories. All terms use the existing normalization by the log of the number of parseable draws.

| Ambiguous translation level | Statements | Accepted classes | Outside-set classes | Total entropy | Within accepted | Within outside set | Accepted/outside split |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | 32 | 1.625 | 0.000 | 0.059 | 0.059 | 0.000 | 0.000 |
| 2 | 14 | 1.643 | 0.857 | 0.107 | 0.073 | 0.001 | 0.033 |
| 3 | 5 | 1.600 | 3.400 | 0.236 | 0.073 | 0.047 | 0.117 |
| 4 | 4 | 1.250 | 2.000 | 0.211 | 0.010 | 0.032 | 0.170 |
| 5 | 4 | 0.500 | 6.250 | 0.323 | 0.000 | 0.242 | 0.081 |

Metrics pool the five models within each statement and then average across statements. At level 5, all four statements showed zero diversity within their accepted draws. Diversity within outside-set classes accounted for about 75% of total entropy. Translation levels use the same outcomes summarized here, so these rows describe the source of diversity. Blind adjudication of frequent outside-set classes could change the interpretation, especially around temporal boundaries and missing readings.

## Can output diversity detect ambiguity beyond wording cues?

Use leave-one-family-out evaluation with fixed class-balanced logistic regression. Fit vectorization and scaling within each fold. The wording baseline uses character 3–5-gram TF-IDF, word count, and proposition count. The output features are normalized entropy, second-largest class share, and the share of parsed draws in classes found by at least two models. The predictors require no gold formulas at inference.

| Features | AUROC | Mean family AUROC | Average precision |
|---|---:|---:|---:|
| Word count and proposition count | 0.722 | 0.809 | 0.465 |
| Output diversity | 0.710 | 0.739 | 0.561 |
| Wording, word count, and proposition count | 0.768 | 0.846 | 0.518 |
| Wording baseline plus output diversity | 0.806 | 0.862 | 0.702 |

The combined model improved AUROC in five families, tied in one, and declined in two. The largest decline was −0.169 for joint_separate. At the fixed 0.5 cutoff, diversity raised false positives from 10 to 15 out of 57 clear statements in pairs with positive reference error and reduced them from 17 to 13 out of 67 clear statements in pairs with zero reference error. This cutoff is uncalibrated. If the gain disappears on independently authored families or increases false clarification requests at matched recall, the finding supports a diagnostic feature with limited value for deciding when to ask.

## Main figure and next validation

Plot mean paired class gaps for zero and positive reference error, split into accepted and outside-set classes, with pair counts and points for each evaluated model. This figure would show what makes up the observed diversity gap on easy and difficult clear rewrites.

The next test needs independent experts to label the wording and adjudicate frequent unmatched formulas without seeing model identities or scores. The retained readings are model-assisted, and holding a model out of the difficulty baseline does not independently validate those readings. Clear rewrites can introduce wording cues. Eight families and four level 5 ambiguous statements limit generalization.

Prior work addresses wrong answers inflating entropy in [ambiguity detection for QA](https://aclanthology.org/2025.trustnlp-main.4/) and distinguishes ambiguity resolution from correction in [interactive temporal-logic translation](https://link.springer.com/chapter/10.1007/978-3-031-37703-7_18). The contribution to test here is the paired NL-to-LTL design and exact semantic accounting of where the diversity comes from.

## Reproduction

From the repository root, run `/opt/miniconda3/envs/ltl/bin/python analyze_difficulty_ambiguity.py`.

The script recomputes semantic classes from 9,150 cached draws and checks class counts, entropies, accuracy, and parse counts for all 915 model–statement results against saved metrics. It verifies the entropy identity and recomputes each held-out pair error from raw scores. A manual smoke check recovered two accepted classes with zero errors, ten identical wrong outputs with zero entropy, and an unparseable output.
