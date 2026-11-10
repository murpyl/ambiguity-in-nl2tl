# Detailed correlation statistics

All values below were reconstructed from the per-model CSVs produced by the saved command run. P-values are shown with more precision than the console output; values printed as 0.000 in the console are not zero. Each model has 124 clear and 59 ambiguous statements, 10 samples per statement, and 59 complete paired comparisons.

## Descriptive statistics

| Model | Metric | Clear mean ± SD | Ambiguous mean ± SD |
|---|---|---:|---:|
| Claude | Classes | 1.185 ± 0.516 | 1.542 ± 1.072 |
| Claude | Entropy | 0.035 ± 0.096 | 0.096 ± 0.178 |
| Claude | Majority share | 0.965 ± 0.104 | 0.903 ± 0.183 |
| Claude | Parse failures | 0.000 ± 0.000 | 0.000 ± 0.000 |
| Claude | Accuracy | 0.884 ± 0.296 | 0.859 ± 0.298 |
| DeepSeek | Classes | 1.218 ± 0.578 | 1.525 ± 0.796 |
| DeepSeek | Entropy | 0.040 ± 0.106 | 0.101 ± 0.145 |
| DeepSeek | Majority share | 0.962 ± 0.106 | 0.902 ± 0.149 |
| DeepSeek | Parse failures | 0.032 ± 0.177 | 0.068 ± 0.254 |
| DeepSeek | Accuracy | 0.912 ± 0.241 | 0.892 ± 0.253 |
| Gemini | Classes | 1.081 ± 0.328 | 1.288 ± 0.559 |
| Gemini | Entropy | 0.016 ± 0.063 | 0.054 ± 0.107 |
| Gemini | Majority share | 0.984 ± 0.073 | 0.944 ± 0.125 |
| Gemini | Parse failures | 0.000 ± 0.000 | 0.000 ± 0.000 |
| Gemini | Accuracy | 0.947 ± 0.200 | 0.925 ± 0.254 |
| GPT Luna | Classes | 1.210 ± 0.530 | 1.390 ± 0.743 |
| GPT Luna | Entropy | 0.039 ± 0.100 | 0.073 ± 0.130 |
| GPT Luna | Majority share | 0.964 ± 0.098 | 0.930 ± 0.128 |
| GPT Luna | Parse failures | 0.008 ± 0.090 | 0.017 ± 0.130 |
| GPT Luna | Accuracy | 0.870 ± 0.310 | 0.890 ± 0.292 |
| Qwen | Classes | 1.250 ± 0.645 | 1.763 ± 0.878 |
| Qwen | Entropy | 0.047 ± 0.109 | 0.151 ± 0.163 |
| Qwen | Majority share | 0.952 ± 0.119 | 0.842 ± 0.178 |
| Qwen | Parse failures | 0.000 ± 0.000 | 0.000 ± 0.000 |
| Qwen | Accuracy | 0.877 ± 0.288 | 0.888 ± 0.272 |

## Unpaired comparisons

| Model | Metric | MWU p | Rank-biserial | Spearman rho | Spearman p |
|---|---|---:|---:|---:|---:|
| Claude | Classes | 0.0173299 | +0.146 | +0.177 | 0.0168097 |
| Claude | Entropy | 0.0151874 | +0.149 | +0.180 | 0.0146844 |
| Claude | Majority share | 0.0166337 | -0.147 | -0.178 | 0.0161187 |
| Claude | Parse failures | 1 | +0.000 | +nan | nan |
| Claude | Accuracy | 0.240059 | -0.075 | -0.087 | 0.240245 |
| DeepSeek | Classes | 0.000419426 | +0.241 | +0.262 | 0.000346893 |
| DeepSeek | Entropy | 0.000334339 | +0.246 | +0.266 | 0.000272498 |
| DeepSeek | Majority share | 0.000292874 | -0.248 | -0.269 | 0.000236597 |
| DeepSeek | Parse failures | 0.27493 | +0.036 | +0.081 | 0.274272 |
| DeepSeek | Accuracy | 0.229644 | -0.079 | -0.089 | 0.229833 |
| Gemini | Classes | 0.000384411 | +0.187 | +0.263 | 0.000315406 |
| Gemini | Entropy | 0.000425358 | +0.186 | +0.261 | 0.000351282 |
| Gemini | Majority share | 0.000400811 | -0.187 | -0.263 | 0.000329755 |
| Gemini | Parse failures | 1 | +0.000 | +nan | nan |
| Gemini | Accuracy | 0.861142 | +0.008 | +0.013 | 0.859383 |
| GPT Luna | Classes | 0.026921 | +0.142 | +0.164 | 0.0263682 |
| GPT Luna | Entropy | 0.0224807 | +0.147 | +0.169 | 0.0219393 |
| GPT Luna | Majority share | 0.0194004 | -0.150 | -0.173 | 0.0188723 |
| GPT Luna | Parse failures | 0.595732 | +0.009 | +0.040 | 0.591387 |
| GPT Luna | Accuracy | 0.700045 | +0.024 | +0.029 | 0.69954 |
| Qwen | Classes | 6.45151e-07 | +0.366 | +0.369 | 2.7304e-07 |
| Qwen | Entropy | 7.67977e-07 | +0.367 | +0.367 | 3.33371e-07 |
| Qwen | Majority share | 6.66527e-07 | -0.369 | -0.369 | 2.83458e-07 |
| Qwen | Parse failures | 1 | +0.000 | +nan | nan |
| Qwen | Accuracy | 0.561317 | -0.040 | -0.043 | 0.561401 |

## Paired comparisons

| Model | Metric | Mean ambiguous minus mean clear | Wilcoxon p |
|---|---|---:|---:|
| Claude | Classes | +0.347458 | 0.00483548 |
| Claude | Entropy | +0.059927 | 0.00422981 |
| Claude | Majority share | -0.060169 | 0.0281845 |
| Claude | Parse failures | +0.000000 | 1 |
| Claude | Accuracy | -0.018644 | 0.774604 |
| DeepSeek | Classes | +0.299435 | 0.00243266 |
| DeepSeek | Entropy | +0.059378 | 0.00208923 |
| DeepSeek | Majority share | -0.059040 | 0.00368268 |
| DeepSeek | Parse failures | +0.033898 | 0.25964 |
| DeepSeek | Accuracy | -0.016667 | 0.913736 |
| Gemini | Classes | +0.203390 | 0.00472255 |
| Gemini | Entropy | +0.038014 | 0.0109095 |
| Gemini | Majority share | -0.038983 | 0.0151441 |
| Gemini | Parse failures | +0.000000 | 1 |
| Gemini | Accuracy | -0.018644 | 0.755071 |
| GPT Luna | Classes | +0.172316 | 0.0449988 |
| GPT Luna | Entropy | +0.032805 | 0.0540904 |
| GPT Luna | Majority share | -0.032392 | 0.0753935 |
| GPT Luna | Parse failures | +0.008475 | 0.654721 |
| GPT Luna | Accuracy | +0.025989 | 0.210308 |
| Qwen | Classes | +0.502825 | 2.61153e-06 |
| Qwen | Entropy | +0.102446 | 7.16844e-06 |
| Qwen | Majority share | -0.107062 | 2.70184e-05 |
| Qwen | Parse failures | +0.000000 | 1 |
| Qwen | Accuracy | +0.016667 | 0.207842 |

## Semantic classes versus accuracy

| Model | Spearman rho |
|---|---:|
| Claude | -0.849 |
| DeepSeek | -0.693 |
| Gemini | -0.494 |
| GPT Luna | -0.763 |
| Qwen | -0.701 |

## Reading the statistics

- n_classes counts distinct semantic meanings among parseable samples, using exact Spot equivalence.
- norm_entropy measures dispersion among valid answers, divided by log(number of valid samples). Zero means one class. For ten valid answers split evenly over two classes, the score is about 0.301, not 1.
- majority_share is the fraction of parseable answers in the largest semantic class; it is not accuracy.
- n_unparsed counts invalid formulas per statement. Across all samples there are eight DeepSeek and two GPT Luna parse failures.
- gold_acc is the fraction of all sampled answers matching a retained target; unparseable answers count as incorrect. Clear rows have one target; ambiguous rows can match any retained target.
- SD measures variation between statements, not uncertainty in the mean.
- MWU compares ranks in the 59 ambiguous versus 124 clear rows. Rank-biserial values are positive when ambiguous values tend higher. Spearman rho correlates each metric with the binary ambiguity label.
- Paired rows first average the clear rewrites within each source item, then compare its ambiguous statement with that average. Each source item therefore gets equal weight.
- Wilcoxon uses ranks of nonzero paired differences; it does not directly test the displayed arithmetic mean. P-values are not probabilities that the null hypothesis is true.
- Parse-failure Spearman values are undefined (nan) when all counts are zero. These explain the command warnings.
- The command reports unadjusted p-values. Bonferroni across five class-count paired tests retains all except GPT Luna; across all 25 paired metric/model tests, only Qwen’s three diversity metrics meet the 0.002 threshold. Neither adjustment resolves within-family dependence.
- The eight shared ambiguity families, related metric definitions, and use of the same models to construct the retained gold set limit generalization. The sample-level tests do not establish model-ranking significance or causal effects.
- This command measures diversity and individual-sample accuracy, not whether majority voting improves accuracy as k increases.
