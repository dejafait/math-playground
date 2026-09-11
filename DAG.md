# Lemma DAG

This is the sole canonical graph: node declarations, file targets, and direct dependency edges are maintained only in the Mermaid block below. `A --> B` means that B uses A as a mathematical input (including a definition or a reused proof argument). Plain-text citations inside proofs are not a second graph. Shared standard inputs are documented in [foundations](foundations/notation-and-inputs.md), outside this graph of proved results.

Graph membership records the informal mathematical argument, not completion of Lean validation. Formalization status lives in each lemma file; the loop must clear the full Lean backlog before new research. All lemma nodes and Corollary 32a are represented. Corollary 32a proves an equivalence only; all-degree positivity and RH remain unproved and are not established input nodes. Where diagram links are unavailable, the `click` lines provide the relative file paths.

```mermaid
flowchart TD
  L231["L231: paired Fourier second-derivative budget"]
  click L231 "lemmas/L231-second-derivative-budget-for-the-paired-fourier-sum.md"
  L227 & L228 & L230 --> L231
  L230["L230: finite Fourier endpoint control"]
  click L230 "lemmas/L230-finite-fourier-reduction-with-endpoint-control.md"
  L227 & L228 & L229 --> L230
  L229["L229: large-divisor paired cell tail"]
  click L229 "lemmas/L229-large-divisor-tail-for-the-paired-cell-discrepancy.md"
  L227 & L228 --> L229
  L228["L228: coprime divisor-phase discrepancy"]
  click L228 "lemmas/L228-coprime-divisor-phase-discrepancy.md"
  L221 & L225 & L227 --> L228
  L227["L227: constant height and separated real benchmark"]
  click L227 "lemmas/L227-constant-height-and-separated-real-benchmark.md"
  L220 & L221 & L223 & L224 & L226 --> L227
  L226["L226: negligible transition weight loss"]
  click L226 "lemmas/L226-negligible-transition-weight-loss.md"
  L220 & L221 & L223 & L225 --> L226
  L225["L225: fractional-part weighted cell occupancy"]
  click L225 "lemmas/L225-fractional-part-weighted-cell-occupancy.md"
  L220 & L223 & L224 --> L225
  L224["L224: paired endpoint sum by square-root cells"]
  click L224 "lemmas/L224-paired-endpoint-sum-by-square-root-cells.md"
  L220 & L221 & L223 --> L224
  L223["L223: unit-progression Bernoulli endpoint formula"]
  click L223 "lemmas/L223-unit-progression-bernoulli-endpoint-formula.md"
  L220 & L221 --> L223
  L222["L222: interior averaged progression-error budget"]
  click L222 "lemmas/L222-interior-averaged-progression-error-budget.md"
  L220 & L221 --> L222
  L221["L221: real main term exceeds the target scale"]
  click L221 "lemmas/L221-real-main-term-exceeds-the-target-scale.md"
  L181 & L218 & L220 --> L221
  L220["L220: weighted inverse-interval discrepancy"]
  click L220 "lemmas/L220-weighted-inverse-interval-discrepancy.md"
  L191 & L218 & L219 --> L220
  L001["L001: an absolutely convergent reciprocal"]
  click L001 "lemmas/L001-an-absolutely-convergent-reciprocal.md"
  L002["L002: conjugation preserves zeros and multiplicities"]
  click L002 "lemmas/L002-conjugation-preserves-zeros-and-multiplicities.md"
  L003["L003: reflection orbits in the open critical strip"]
  click L003 "lemmas/L003-reflection-orbits-in-the-open-critical-strip.md"
  L004["L004: a counterexample to the symmetry-only inference"]
  click L004 "lemmas/L004-a-counterexample-to-the-symmetry-only-inference.md"
  L005["L005: the Euler-product logarithm on its actual domain"]
  click L005 "lemmas/L005-the-euler-product-logarithm-on-its-actual-domain.md"
  L006["L006: a nonnegative trigonometric polynomial gives a product inequality"]
  click L006 "lemmas/L006-a-nonnegative-trigonometric-polynomial-gives-a-product-inequality.md"
  L007["L007: nonvanishing on Re(s)=1"]
  click L007 "lemmas/L007-nonvanishing-on-re-s-1.md"
  L008["L008: residue at 1 and the value at 0"]
  click L008 "lemmas/L008-residue-at-1-and-the-value-at-0.md"
  L009["L009: complete classification outside the open strip"]
  click L009 "lemmas/L009-complete-classification-outside-the-open-strip.md"
  L010["L010: the positive prime-logarithm representation diverges at and left of 1"]
  click L010 "lemmas/L010-the-positive-prime-logarithm-representation-diverges-at-and-left-of-1.md"
  L011["L011: the continued product inequality is false"]
  click L011 "lemmas/L011-the-continued-product-inequality-is-false.md"
  L012["L012: a convergent alternating representation in Re(s)>0"]
  click L012 "lemmas/L012-a-convergent-alternating-representation-in-re-s-0.md"
  L013["L013: no real zeros in the open strip"]
  click L013 "lemmas/L013-no-real-zeros-in-the-open-strip.md"
  L014["L014: a positive-kernel Laplace representation"]
  click L014 "lemmas/L014-a-positive-kernel-laplace-representation.md"
  L015["L015: a nonnegative indicator kernel can have zeros inside the strip"]
  click L015 "lemmas/L015-a-nonnegative-indicator-kernel-can-have-zeros-inside-the-strip.md"
  L016["L016: theta transformation and exponential tails"]
  click L016 "lemmas/L016-theta-transformation-and-exponential-tails.md"
  L017["L017: split Mellin integral with entire remainder"]
  click L017 "lemmas/L017-split-mellin-integral-with-entire-remainder.md"
  L018["L018: entire completion and exact zero correspondence"]
  click L018 "lemmas/L018-entire-completion-and-exact-zero-correspondence.md"
  L019["L019: the theta boundary derivative and a positive kernel"]
  click L019 "lemmas/L019-the-theta-boundary-derivative-and-a-positive-kernel.md"
  L020["L020: entire Fourier cosine representation of Ξ"]
  click L020 "lemmas/L020-entire-fourier-cosine-representation-of.md"
  L021["L021: imaginary-axis positivity and moment coefficients"]
  click L021 "lemmas/L021-imaginary-axis-positivity-and-moment-coefficients.md"
  L022["L022: positive smooth superexponential kernels do not force real zeros"]
  click L022 "lemmas/L022-positive-smooth-superexponential-kernels-do-not-force-real-zeros.md"
  L023["L023: an unconditional entire growth bound"]
  click L023 "lemmas/L023-an-unconditional-entire-growth-bound.md"
  L024["L024: an unconditional paired Hadamard product"]
  click L024 "lemmas/L024-an-unconditional-paired-hadamard-product.md"
  L025["L025: moment coefficients and reciprocal-zero power sums"]
  click L025 "lemmas/L025-moment-coefficients-and-reciprocal-zero-power-sums.md"
  L026["L026: an elementary zero-free rectangle for Ξ"]
  click L026 "lemmas/L026-an-elementary-zero-free-rectangle-for.md"
  L027["L027: six positive reciprocal-power sums and a strict moment inequality"]
  click L027 "lemmas/L027-six-positive-reciprocal-power-sums-and-a-strict-moment-inequality.md"
  L028["L028: a degree-two Jensen polynomial is real-rooted"]
  click L028 "lemmas/L028-a-degree-two-jensen-polynomial-is-real-rooted.md"
  L029["L029: even all positive scalar power sums do not force real zeros"]
  click L029 "lemmas/L029-even-all-positive-scalar-power-sums-do-not-force-real-zeros.md"
  L030["L030: convergent mixed quadratic forms"]
  click L030 "lemmas/L030-convergent-mixed-quadratic-forms.md"
  L031["L031: a mixed test detects the finite counterexample"]
  click L031 "lemmas/L031-a-mixed-test-detects-the-finite-counterexample.md"
  L032["L032: polynomial detection of a nonreal summable node"]
  click L032 "lemmas/L032-polynomial-detection-of-a-nonreal-summable-node.md"
  C032a["C032a: an explicit RH-equivalent condition, not a proof of it"]
  click C032a "lemmas/C032a-an-explicit-rh-equivalent-condition-not-a-proof-of-it.md"
  L033["L033: the first mixed determinant in moment coordinates"]
  click L033 "lemmas/L033-the-first-mixed-determinant-in-moment-coordinates.md"
  L034["L034: small zero arguments do not ensure a mixed determinant sign"]
  click L034 "lemmas/L034-small-zero-arguments-do-not-ensure-a-mixed-determinant-sign.md"
  L035["L035: explicit uniform tails for the first five moments"]
  click L035 "lemmas/L035-explicit-uniform-tails-for-the-first-five-moments.md"
  L036["L036: validated midpoint Taylor panels"]
  click L036 "lemmas/L036-validated-midpoint-taylor-panels.md"
  L037["L037: enclosures used by the finite certificate"]
  click L037 "lemmas/L037-enclosures-used-by-the-finite-certificate.md"
  L038["L038: a certified positive first mixed determinant"]
  click L038 "lemmas/L038-a-certified-positive-first-mixed-determinant.md"
  L039["L039: moment tails through any fixed even degree"]
  click L039 "lemmas/L039-moment-tails-through-any-fixed-even-degree.md"
  L040["L040: a justified finite Newton recurrence"]
  click L040 "lemmas/L040-a-justified-finite-newton-recurrence.md"
  L041["L041: a certified positive H_2 test"]
  click L041 "lemmas/L041-a-certified-positive-h-2-test.md"
  L042["L042: absolutely convergent Vandermonde expansion"]
  click L042 "lemmas/L042-absolutely-convergent-vandermonde-expansion.md"
  L043["L043: ordinary moment matrices are strictly positive definite"]
  click L043 "lemmas/L043-ordinary-moment-matrices-are-strictly-positive-definite.md"
  L044["L044: ordinary Gram positivity does not survive the needed logarithm map"]
  click L044 "lemmas/L044-ordinary-gram-positivity-does-not-survive-the-needed-logarithm-map.md"
  L045["L045: strict log-concavity of each theta-kernel summand"]
  click L045 "lemmas/L045-strict-log-concavity-of-each-theta-kernel-summand.md"
  L046["L046: the variance obstruction in a sum of log-concave terms"]
  click L046 "lemmas/L046-the-variance-obstruction-in-a-sum-of-log-concave-terms.md"
  L047["L047: strict log-concavity of the full theta kernel"]
  click L047 "lemmas/L047-strict-log-concavity-of-the-full-theta-kernel.md"
  L048["L048: smooth even extension and monotonicity of K"]
  click L048 "lemmas/L048-smooth-even-extension-and-monotonicity-of-k.md"
  L049["L049: strict log-concavity alone still does not force real zeros"]
  click L049 "lemmas/L049-strict-log-concavity-alone-still-does-not-force-real-zeros.md"
  L050["L050: a small superexponential mixture remains strictly log-concave"]
  click L050 "lemmas/L050-a-small-superexponential-mixture-remains-strictly-log-concave.md"
  L051["L051: order at most one for superexponential Fourier kernels"]
  click L051 "lemmas/L051-order-at-most-one-for-superexponential-fourier-kernels.md"
  L052["L052: tuning the introduced zeros into the strip"]
  click L052 "lemmas/L052-tuning-the-introduced-zeros-into-the-strip.md"
  L053["L053: a differential equation for the comparison base transform"]
  click L053 "lemmas/L053-a-differential-equation-for-the-comparison-base-transform.md"
  L054["L054: every comparison-base zero is real and outside the small rectangle"]
  click L054 "lemmas/L054-every-comparison-base-zero-is-real-and-outside-the-small-rectangle.md"
  L055["L055: the combined generic conditions admit nonreal zeros"]
  click L055 "lemmas/L055-the-combined-generic-conditions-admit-nonreal-zeros.md"
  L056["L056: every finite comparison-base Hankel matrix is positive definite"]
  click L056 "lemmas/L056-every-finite-comparison-base-hankel-matrix-is-positive-definite.md"
  L057["L057: any fixed number of Hankel tests can coexist with nonreal zeros"]
  click L057 "lemmas/L057-any-fixed-number-of-hankel-tests-can-coexist-with-nonreal-zeros.md"
  L058["L058: heat deformation and local zero motion"]
  click L058 "lemmas/L058-heat-deformation-and-local-zero-motion.md"
  L059["L059: local splitting at a real double zero"]
  click L059 "lemmas/L059-local-splitting-at-a-real-double-zero.md"
  L060["L060: local splitting at a real multiple zero"]
  click L060 "lemmas/L060-local-splitting-at-a-real-multiple-zero.md"
  L061["L061: bounded-domain forward continuation"]
  click L061 "lemmas/L061-bounded-domain-forward-continuation.md"
  L062["L062: conditional whole-plane forward continuation"]
  click L062 "lemmas/L062-conditional-whole-plane-forward-continuation.md"
  L063["L063: uniform growth and paired products for heat slices"]
  click L063 "lemmas/L063-uniform-growth-and-paired-products-for-heat-slices.md"
  L064["L064: paired-zero interaction and local motion"]
  click L064 "lemmas/L064-paired-zero-interaction-and-local-motion.md"
  L065["L065: sign of a nonreal quartet contribution"]
  click L065 "lemmas/L065-sign-of-a-nonreal-quartet-contribution.md"
  L066["L066: imaginary motion at a highest simple zero"]
  click L066 "lemmas/L066-imaginary-motion-at-a-highest-simple-zero.md"
  L067["L067: conditional motion near a strip supremum"]
  click L067 "lemmas/L067-conditional-motion-near-a-strip-supremum.md"
  L068["L068: sparse product with large upward contribution"]
  click L068 "lemmas/L068-sparse-product-with-large-upward-contribution.md"
  L069["L069: positive divergence of the full sparse interaction"]
  click L069 "lemmas/L069-positive-divergence-of-the-full-sparse-interaction.md"
  L070["L070: vanishing upward contribution at upper sparse zeros"]
  click L070 "lemmas/L070-vanishing-upward-contribution-at-upper-sparse-zeros.md"
  L071["L071: quadratically penalized height maxima"]
  click L071 "lemmas/L071-quadratically-penalized-height-maxima.md"
  L072["L072: fixed-product obstruction to penalized upward vanishing"]
  click L072 "lemmas/L072-fixed-product-obstruction-to-penalized-upward-vanishing.md"
  L073["L073: favorable penalties for upper satellites"]
  click L073 "lemmas/L073-favorable-penalties-for-upper-satellites.md"
  L074["L074: finite successor windows cannot sustain upward motion"]
  click L074 "lemmas/L074-finite-successor-windows-cannot-sustain-upward-motion.md"
  L075["L075: hidden satellites obstruct all penalty subsequences"]
  click L075 "lemmas/L075-hidden-satellites-obstruct-all-penalty-subsequences.md"
  L076["L076: full upward subsequence under bounded local count"]
  click L076 "lemmas/L076-full-upward-subsequence-under-bounded-local-count.md"
  L077["L077: full upward subsequence with growing local counts"]
  click L077 "lemmas/L077-full-upward-subsequence-with-growing-local-counts.md"
  L078["L078: rate-free upward subsequence at power coordinates"]
  click L078 "lemmas/L078-rate-free-upward-subsequence-at-power-coordinates.md"
  L079["L079: rate-free upward averaging for all summable powers"]
  click L079 "lemmas/L079-rate-free-upward-averaging-for-all-summable-powers.md"
  L080["L080: upward averaging at logarithmic square-root coordinates"]
  click L080 "lemmas/L080-upward-averaging-at-logarithmic-square-root-coordinates.md"
  L081["L081: upward averaging at iterated-log coordinates"]
  click L081 "lemmas/L081-upward-averaging-at-iterated-log-coordinates.md"
  L082["L082: upward averaging for monotone square-root multipliers"]
  click L082 "lemmas/L082-upward-averaging-for-monotone-square-root-multipliers.md"
  L083["L083: close pairs obstruct unrestricted upward averaging"]
  click L083 "lemmas/L083-close-pairs-obstruct-unrestricted-upward-averaging.md"
  L084["L084: upward subsequence from suffix-minimum coordinates"]
  click L084 "lemmas/L084-upward-subsequence-from-suffix-minimum-coordinates.md"
  L085["L085: obstruction to height-normalized suffix minima"]
  click L085 "lemmas/L085-obstruction-to-height-normalized-suffix-minima.md"
  L086["L086: increment-sensitive upward bound at suffix minima"]
  click L086 "lemmas/L086-increment-sensitive-upward-bound-at-suffix-minima.md"
  L087["L087: sparse suffix minima obstruct increment-bound selection"]
  click L087 "lemmas/L087-sparse-suffix-minima-obstruct-increment-bound-selection.md"
  L088["L088: actual upward subsequence at sparse suffix minima"]
  click L088 "lemmas/L088-actual-upward-subsequence-at-sparse-suffix-minima.md"
  L089["L089: upward averaging at dense suffix minima"]
  click L089 "lemmas/L089-upward-averaging-at-dense-suffix-minima.md"
  L090["L090: upward averaging on selected irregular blocks"]
  click L090 "lemmas/L090-upward-averaging-on-selected-irregular-blocks.md"
  L091["L091: height-budget selection on irregular blocks"]
  click L091 "lemmas/L091-height-budget-selection-on-irregular-blocks.md"
  L092["L092: spacing-sensitive height-budget selection"]
  click L092 "lemmas/L092-spacing-sensitive-height-budget-selection.md"
  L093["L093: separated suffix blocks realize the spacing criterion"]
  click L093 "lemmas/L093-separated-suffix-blocks-realize-the-spacing-criterion.md"
  L094["L094: exact crowding height-budget selection"]
  click L094 "lemmas/L094-exact-crowding-height-budget-selection.md"
  L095["L095: paired suffix blocks realize exact crowding"]
  click L095 "lemmas/L095-paired-suffix-blocks-realize-exact-crowding.md"
  L096["L096: selected-subset crowding selection"]
  click L096 "lemmas/L096-selected-subset-crowding-selection.md"
  L097["L097: endpoint packets realize subset selection"]
  click L097 "lemmas/L097-endpoint-packets-realize-subset-selection.md"
  L098["L098: consecutive packets obstruct optimized subset criteria"]
  click L098 "lemmas/L098-consecutive-packets-obstruct-optimized-subset-criteria.md"
  L099["L099: common upward subsequence at consecutive packet endpoints"]
  click L099 "lemmas/L099-common-upward-subsequence-at-consecutive-packet-endpoints.md"
  L100["L100: upward averaging for arbitrary prescribed interpolation"]
  click L100 "lemmas/L100-upward-averaging-for-arbitrary-prescribed-interpolation.md"
  L101["L101: upward selection inside arbitrary prescribed sets"]
  click L101 "lemmas/L101-upward-selection-inside-arbitrary-prescribed-sets.md"
  L102["L102: no common upward subsequence at power coordinates"]
  click L102 "lemmas/L102-no-common-upward-subsequence-at-power-coordinates.md"
  L103["L103: unbounded successor gaps do not give common selection"]
  click L103 "lemmas/L103-unbounded-successor-gaps-do-not-give-common-selection.md"
  L104["L104: inverse-square criterion for common upward selection"]
  click L104 "lemmas/L104-inverse-square-criterion-for-common-upward-selection.md"
  L105["L105: integer-gap criterion for common prescribed selection"]
  click L105 "lemmas/L105-integer-gap-criterion-for-common-prescribed-selection.md"
  L106["L106: common selection for general summable coordinates"]
  click L106 "lemmas/L106-common-selection-for-general-summable-coordinates.md"
  L107["L107: forward-jump obstruction to upward selection"]
  click L107 "lemmas/L107-forward-jump-obstruction-to-upward-selection.md"
  L108["L108: nonexplosion under power gap lower bounds"]
  click L108 "lemmas/L108-nonexplosion-under-power-gap-lower-bounds.md"
  L109["L109: nonexplosion for sublinear polynomial cluster counts"]
  click L109 "lemmas/L109-nonexplosion-for-sublinear-polynomial-cluster-counts.md"
  L110["L110: nonexplosion for logarithmic cluster counts"]
  click L110 "lemmas/L110-nonexplosion-for-logarithmic-cluster-counts.md"
  L111["L111: adaptive payoff for summable linearly bounded clusters"]
  click L111 "lemmas/L111-adaptive-payoff-for-summable-linearly-bounded-clusters.md"
  L112["L112: bounded-generator payoff for dyadic spikes"]
  L113["L113: bounded-generator payoff for arbitrary lacunary masses"]
  click L112 "lemmas/L112-bounded-generator-payoff-for-dyadic-spikes.md"
  click L113 "lemmas/L113-bounded-generator-payoff-for-arbitrary-lacunary-masses.md"
  L114["L114: bounded-generator payoff for separated mass pairs"]
  click L114 "lemmas/L114-bounded-generator-payoff-for-separated-mass-pairs.md"
  L115["L115: bounded-generator payoff for separated finite blocks"]
  click L115 "lemmas/L115-bounded-generator-payoff-for-separated-finite-blocks.md"
  L116["L116: weak blocks obstruct endpoint-only payoffs"]
  click L116 "lemmas/L116-weak-blocks-obstruct-endpoint-only-payoffs.md"
  L117["L117: dyadic block payoffs are equivalent to unrestricted payoffs"]
  click L117 "lemmas/L117-dyadic-block-payoffs-are-equivalent-to-unrestricted-payoffs.md"
  L118["L118: finite capacity and summable cover alternative"]
  click L118 "lemmas/L118-finite-capacity-and-summable-cover-alternative.md"
  L119["L119: vanishing dual cuts and unrestricted payoffs"]
  click L119 "lemmas/L119-vanishing-dual-cuts-and-unrestricted-payoffs.md"
  L120["L120: nonexplosion for unrestricted separated cluster counts"]
  click L120 "lemmas/L120-nonexplosion-for-unrestricted-separated-cluster-counts.md"
  L121["L121: exact-distance capacity alternative"]
  click L121 "lemmas/L121-exact-distance-capacity-alternative.md"
  L122["L122: vanishing exact-distance cuts for arbitrary coordinates"]
  click L122 "lemmas/L122-vanishing-exact-distance-cuts-for-arbitrary-coordinates.md"
  L123["L123: nonexplosion for arbitrary summable coordinates"]
  click L123 "lemmas/L123-nonexplosion-for-arbitrary-summable-coordinates.md"
  L124["L124: upward selection for arbitrary bounded heights"]
  click L124 "lemmas/L124-upward-selection-for-arbitrary-bounded-heights.md"
  L125["L125: upward selection for strip zero multisets"]
  click L125 "lemmas/L125-upward-selection-for-strip-zero-multisets.md"
  L126["L126: fixed-slice motion selection and supremum obstruction"]
  click L126 "lemmas/L126-fixed-slice-motion-selection-and-supremum-obstruction.md"
  L127["L127: forward splitting and height at a nonreal multiple zero"]
  click L127 "lemmas/L127-forward-splitting-and-height-at-a-nonreal-multiple-zero.md"
  L128["L128: bounded-domain upper-height derivative"]
  click L128 "lemmas/L128-bounded-domain-upper-height-derivative.md"
  L129["L129: exterior upward interaction in a horizontal window"]
  click L129 "lemmas/L129-exterior-upward-interaction-in-a-horizontal-window.md"
  L130["L130: parameter-uniform reciprocal-square zero tails"]
  click L130 "lemmas/L130-parameter-uniform-reciprocal-square-zero-tails.md"
  L131["L131: growing buffers for uniform exterior interaction"]
  click L131 "lemmas/L131-growing-buffers-for-uniform-exterior-interaction.md"
  L132["L132: critical buffer sharpness for strip multisets"]
  click L132 "lemmas/L132-critical-buffer-sharpness-for-strip-multisets.md"
  L133["L133: local-count exterior interaction and logarithmic buffers"]
  click L133 "lemmas/L133-local-count-exterior-interaction-and-logarithmic-buffers.md"
  L134["L134: logarithmic-buffer sharpness for local counts"]
  click L134 "lemmas/L134-logarithmic-buffer-sharpness-for-local-counts.md"
  L135["L135: recentered Jensen local-count audit"]
  click L135 "lemmas/L135-recentered-jensen-local-count-audit.md"
  L136["L136: undeformed logarithmic Jensen ratio"]
  click L136 "lemmas/L136-undeformed-logarithmic-jensen-ratio.md"
  L137["L137: negative heat convolution and cancellation"]
  click L137 "lemmas/L137-negative-heat-convolution-and-cancellation.md"
  L138["L138: fixed negative-heat center expansion"]
  click L138 "lemmas/L138-fixed-negative-heat-center-expansion.md"
  L139["L139: absolute series mass and dominance obstruction"]
  click L139 "lemmas/L139-absolute-series-mass-and-dominance-obstruction.md"
  L140["L140: Poisson representation with controlled tail"]
  click L140 "lemmas/L140-poisson-representation-with-controlled-tail.md"
  L141["L141: uniform central-mode stationary phase"]
  click L141 "lemmas/L141-uniform-central-mode-stationary-phase.md"
  L142["L142: exponentially small negative Poisson modes"]
  click L142 "lemmas/L142-exponentially-small-negative-poisson-modes.md"
  L143["L143: all-positive-mode stationary phase"]
  click L143 "lemmas/L143-all-positive-mode-stationary-phase.md"
  L144["L144: Gaussian-weighted dual Dirichlet series"]
  click L144 "lemmas/L144-gaussian-weighted-dual-dirichlet-series.md"
  L145["L145: Mellin contour and pole-scale audit"]
  click L145 "lemmas/L145-mellin-contour-and-pole-scale-audit.md"
  L147["L147: first correction to the negative-heat center"]
  click L147 "lemmas/L147-first-correction-to-the-negative-heat-center.md"
  L148["L148: correction mass and leading-sum threshold"]
  click L148 "lemmas/L148-correction-mass-and-leading-sum-threshold.md"
  L149["L149: dyadic mean square with moving weights"]
  click L149 "lemmas/L149-dyadic-mean-square-with-moving-weights.md"
  L150["L150: dyadic fourth moment with divisor loss"]
  click L150 "lemmas/L150-dyadic-fourth-moment-with-divisor-loss.md"
  L151["L151: exact multiplicative diagonal has one logarithm"]
  click L151 "lemmas/L151-exact-multiplicative-diagonal.md"
  L152["L152: Gaussian fourth moment with two logarithms"]
  click L152 "lemmas/L152-gaussian-fourth-moment-with-two-logarithms.md"
  L153["L153: Hilbert cancellation for the Gaussian fourth moment"]
  click L153 "lemmas/L153-hilbert-cancellation-for-the-gaussian-fourth-moment.md"
  L154["L154: moment information and a truncated-tail criterion"]
  click L154 "lemmas/L154-moment-information-and-a-truncated-tail-criterion.md"
  L155["L155: Gaussian-window reduction for truncated tails"]
  click L155 "lemmas/L155-gaussian-window-reduction-for-truncated-tails.md"
  L156["L156: smooth amplitude cutoff variation cost"]
  click L156 "lemmas/L156-smooth-amplitude-cutoff-variation-cost.md"
  L157["L157: signed cutoff Hilbert remainder"]
  click L157 "lemmas/L157-signed-cutoff-hilbert-remainder.md"
  L158["L158: quartic symmetrization retains small denominators"]
  click L158 "lemmas/L158-quartic-symmetrization-retains-small-denominators.md"
  L159["L159: exact resonant cutoff contribution"]
  click L159 "lemmas/L159-exact-resonant-cutoff-contribution.md"
  L160["L160: total-frequency integration with a cutoff"]
  click L160 "lemmas/L160-total-frequency-integration-with-a-cutoff.md"
  L161["L161: sextic resonance with second cutoff derivative"]
  click L161 "lemmas/L161-sextic-resonance-with-second-cutoff-derivative.md"
  L162["L162: triple-product diagonal bound"]
  click L162 "lemmas/L162-triple-product-diagonal-bound.md"
  L163["L163: restricted triple-product diagonal"]
  click L163 "lemmas/L163-restricted-triple-product-diagonal.md"
  L164["L164: sharpness of the restricted triple diagonal"]
  click L164 "lemmas/L164-sharpness-of-the-restricted-triple-diagonal.md"
  L165["L165: excluded-pair resonant mass sharpness"]
  click L165 "lemmas/L165-excluded-pair-resonant-mass-sharpness.md"
  L166["L166: Gaussian resonant mass does not flatten"]
  click L166 "lemmas/L166-gaussian-resonant-mass-does-not-flatten.md"
  L167["L167: centered-primitive cutoff covariance"]
  click L167 "lemmas/L167-centered-primitive-cutoff-covariance.md"
  L168["L168: blockwise cutoff covariance and local moment gap"]
  click L168 "lemmas/L168-blockwise-cutoff-covariance-and-local-moment-gap.md"
  L169["L169: freezing Gaussian coefficients in cutoff blocks"]
  click L169 "lemmas/L169-freezing-gaussian-coefficients-in-cutoff-blocks.md"
  L170["L170: frozen block variance profile"]
  click L170 "lemmas/L170-frozen-block-variance-profile.md"
  L171["L171: frozen block fourth moment and integrability gap"]
  click L171 "lemmas/L171-frozen-block-fourth-moment-and-integrability-gap.md"
  L172["L172: frozen third moment and first moment test"]
  click L172 "lemmas/L172-frozen-third-moment-and-first-moment-test.md"
  L173["L173: last-block endpoint profile reduction"]
  click L173 "lemmas/L173-last-block-endpoint-profile-reduction.md"
  L174["L174: derivative-test limit for last-block first moments"]
  click L174 "lemmas/L174-derivative-test-limit-for-last-block-first-moments.md"
  L175["L175: last-block stationary transform"]
  click L175 "lemmas/L175-last-block-stationary-transform.md"
  L176["L176: fixed dual interval with small boundary error"]
  click L176 "lemmas/L176-fixed-dual-interval-with-small-boundary-error.md"
  L177["L177: uniform truncated fixed dual interval"]
  click L177 "lemmas/L177-uniform-truncated-fixed-dual-interval.md"
  L178["L178: weighted dual profile and involution"]
  click L178 "lemmas/L178-weighted-dual-profile-and-involution.md"
  L179["L179: profile eigenspaces and first-moment obstruction"]
  click L179 "lemmas/L179-profile-eigenspaces-and-first-moment-obstruction.md"
  L180["L180: mixed fourth-moment kernel expansion"]
  click L180 "lemmas/L180-mixed-fourth-moment-kernel-expansion.md"
  L181["L181: positive quartic stationary product strip"]
  click L181 "lemmas/L181-positive-quartic-stationary-product-strip.md"
  L182["L182: endpoint-uniform quartic stationary phase"]
  click L182 "lemmas/L182-endpoint-uniform-quartic-stationary-phase.md"
  L183["L183: square-product stationary contribution"]
  click L183 "lemmas/L183-square-product-stationary-contribution.md"
  L184["L184: near-square stationary contribution"]
  click L184 "lemmas/L184-near-square-stationary-contribution.md"
  L185["L185: square-displacement short-sum reduction"]
  click L185 "lemmas/L185-square-displacement-short-sum-reduction.md"
  L186["L186: two-factor residue filter for short sums"]
  click L186 "lemmas/L186-two-factor-residue-filter-for-short-sums.md"
  L187["L187: gcd split and large-gcd tail"]
  click L187 "lemmas/L187-gcd-split-and-large-gcd-tail.md"
  L188["L188: coprime quadratic roots in the exact interval"]
  click L188 "lemmas/L188-coprime-quadratic-roots-in-the-exact-interval.md"
  L219["L219: single-factor slice and real-measure obstruction"]
  click L219 "lemmas/L219-single-factor-slice-and-real-measure-obstruction.md"
  L191 & L213 & L218 --> L219
  L218["L218: fixed-box single candidate and square exclusion"]
  click L218 "lemmas/L218-fixed-box-single-candidate-and-square-exclusion.md"
  L191 & L194 & L195 & L213 & L217 --> L218
  L217["L217: exterior bulk majorant and arithmetic threshold"]
  click L217 "lemmas/L217-exterior-bulk-majorant-and-arithmetic-threshold.md"
  L195 & L213 --> L217
  L216["L216: negligible mass near the factor sign boundary"]
  click L216 "lemmas/L216-negligible-mass-near-the-factor-sign-boundary.md"
  L195 & L213 --> L216
  L215["L215: negligible positive mass in exterior endpoint caps"]
  click L215 "lemmas/L215-negligible-positive-mass-in-exterior-endpoint-caps.md"
  L213 --> L215
  L214["L214: positive-factor localization in the exterior"]
  click L214 "lemmas/L214-positive-factor-localization-in-the-exterior.md"
  L195 & L213 --> L214
  L213["L213: exterior positive mass and product localization"]
  click L213 "lemmas/L213-exterior-positive-mass-and-product-localization.md"
  L191 & L195 & L197 --> L213
  L212["L212: negative central-strip mass lower bound"]
  click L212 "lemmas/L212-negative-central-strip-mass-lower-bound.md"
  L188 & L197 & L198 & L199 & L202 & L211 --> L212
  L211["L211: totient threshold on the coprime population"]
  click L211 "lemmas/L211-totient-threshold-on-the-coprime-population.md"
  L202 & L210 --> L211
  L210["L210: positive-proportion coprime factor population"]
  click L210 "lemmas/L210-positive-proportion-coprime-factor-population.md"
  L202 & L205 & L207 & L209 --> L210
  L209["L209: large-prime tail by product counting"]
  click L209 "lemmas/L209-large-prime-tail-by-product-counting.md"
  L202 & L205 --> L209
  L208["L208: opposite-slice extension of the prime band"]
  click L208 "lemmas/L208-opposite-slice-extension-of-the-prime-band.md"
  L202 & L205 & L207 --> L208
  L207["L207: growing prime band with uniform error"]
  click L207 "lemmas/L207-growing-prime-band-with-uniform-error.md"
  L202 & L205 --> L207
  L206["L206: fixed-prime-band joint divisor bound"]
  click L206 "lemmas/L206-fixed-prime-band-joint-divisor-bound.md"
  L202 & L205 --> L206
  L205["L205: fixed-prime selection in factor slices"]
  click L205 "lemmas/L205-fixed-prime-selection-in-factor-slices.md"
  L202 & L203 & L204 --> L205
  L204["L204: positive proportion in quartic factor slices"]
  click L204 "lemmas/L204-positive-proportion-in-quartic-factor-slices.md"
  L202 & L203 --> L204
  L203["L203: factor-slice quartic phase reduction"]
  click L203 "lemmas/L203-factor-slice-quartic-phase-reduction.md"
  L201 & L202 --> L203
  L202["L202: safe factor box before phase selection"]
  click L202 "lemmas/L202-safe-factor-box-before-phase-selection.md"
  L181 & L201 --> L202
  L201["L201: full-core integer phase criterion"]
  click L201 "lemmas/L201-full-core-integer-phase-criterion.md"
  L199 --> L201
  L200["L200: near-diagonal full-core exclusion"]
  click L200 "lemmas/L200-near-diagonal-full-core-exclusion.md"
  L197 & L199 --> L200
  L199["L199: full-core square-root window and coprime error"]
  click L199 "lemmas/L199-full-core-square-root-window-and-coprime-error.md"
  L191 & L194 & L197 & L198 --> L199
  L198["L198: negative-strip lower-bound counting criterion"]
  click L198 "lemmas/L198-negative-strip-lower-bound-counting-criterion.md"
  L178 & L191 & L194 & L195 & L197 --> L198
  L197["L197: averaged floor-cell mass without divisor loss"]
  click L197 "lemmas/L197-averaged-floor-cell-mass-without-divisor-loss.md"
  L191 & L194 & L195 & L196 --> L197
  L196["L196: negative central-strip localization bound"]
  click L196 "lemmas/L196-negative-central-strip-localization-bound.md"
  L191 & L193 & L194 & L195 --> L196
  L195["L195: ordered-pair sign and central strip"]
  click L195 "lemmas/L195-ordered-pair-sign-and-central-strip.md"
  L178 & L179 & L186 & L191 & L193 & L194 --> L195
  L194["L194: positive Fresnel coefficient in the interval mass"]
  click L194 "lemmas/L194-positive-fresnel-coefficient-in-the-interval-mass.md"
  L182 & L185 & L192 & L193 --> L194
  L193["L193: density first-moment decay"]
  click L193 "lemmas/L193-density-first-moment-decay.md"
  L186 & L187 & L191 & L192 --> L193
  L192["L192: coprime density approximation error"]
  click L192 "lemmas/L192-coprime-density-approximation-error.md"
  L185 & L186 & L187 & L190 & L191 --> L192
  L191["L191: exact displacement interval and Möbius sum"]
  click L191 "lemmas/L191-exact-displacement-interval-and-mobius-sum.md"
  L186 & L188 & L190 --> L191
  L190["L190: zero-mode floor cells and signed profile"]
  click L190 "lemmas/L190-zero-mode-floor-cells-and-signed-profile.md"
  L186 & L188 & L189 --> L190
  L189["L189: additive-character expansion of the coprime sector"]
  click L189 "lemmas/L189-additive-character-expansion-of-the-coprime-sector.md"
  L188 --> L189
  L187 --> L188
  L186 --> L187
  L180 & L185 --> L186
  L182 & L184 --> L185
  L182 & L183 --> L184
  L182 --> L183
  L179 & L181 --> L182
  L180 --> L181
  L171 & L179 --> L180
  L173 & L177 & L178 --> L179
  L173 & L177 --> L178
  L174 & L175 & L176 --> L177
  L175 --> L176
  L174 --> L175
  L169 & L170 --> L173
  L171 --> L172
  L169 & L170 --> L171
  L156 & L169 --> L170
  L156 & L166 & L168 --> L169
  L156 & L166 --> L168
  L156 & L166 --> L167
  L155 & L165 --> L166
  L155 & L162 & L164 --> L165
  L163 --> L164
  L156 & L162 --> L163
  L156 & L161 --> L162
  L160 --> L161
  L156 & L157 & L158 & L159 --> L160
  L151 & L156 & L158 --> L159
  L156 & L157 --> L158
  L156 --> L157
  L155 --> L156
  L149 & L154 --> L155
  L149 & L153 --> L154
  L149 & L152 --> L153
  L149 & L150 & L151 --> L152
  L149 --> L151
  L149 --> L150
  L138 --> L149
  L139 & L147 --> L148
  L138 --> L147
  L146["L146: functional equation returns the original series"]
  click L146 "lemmas/L146-functional-equation-returns-the-original-series.md"
  L138 & L140 & L144 & L145 --> L146
  L008 & L144 --> L145
  L138 & L140 & L142 & L143 --> L144
  L140 & L141 --> L143
  L140 --> L142
  L140 --> L141
  L138 --> L140
  L138 --> L139
  L136 & L137 --> L138
  L058 & L136 --> L137
  L001 & L018 & L058 & L135 --> L136
  L058 & L063 --> L135
  L002 --> L003
  L001 & L005 --> L006
  L001 & L006 --> L007
  L001 & L007 & L008 --> L009
  L002 & L008 --> L011
  L008 --> L012
  L009 & L012 --> L013
  L012 --> L014
  L016 --> L017
  L001 & L007 & L009 & L017 --> L018
  L016 --> L019
  L017 & L018 & L019 --> L020
  L019 & L020 --> L021
  L021 --> L022
  L018 & L019 & L020 --> L023
  L018 & L021 & L023 --> L024
  L018 & L021 & L024 --> L025
  L016 & L018 & L020 --> L026
  L019 & L021 & L024 & L025 & L026 --> L027
  L021 & L027 --> L028
  L018 & L024 & L025 --> L030
  L029 & L030 --> L031
  L018 & L024 & L026 & L030 & L032 --> C032a
  L021 & L025 & L027 & L030 --> L033
  L027 --> L034
  L019 & L021 --> L035
  L035 & L036 --> L037
  L027 & L033 & L035 & L036 & L037 --> L038
  L035 --> L039
  L021 & L025 & L030 --> L040
  L030 & L036 & L037 & L039 & L040 --> L041
  L024 & L025 & L027 & L030 --> L042
  L019 & L021 --> L043
  L022 & L043 --> L044
  L035 --> L045
  L045 --> L046
  L045 & L046 --> L047
  L016 & L019 & L047 --> L048
  L044 & L046 --> L049
  L022 & L046 --> L050
  L050 & L051 --> L052
  L052 --> L053
  L053 --> L054
  L021 & L050 & L051 & L052 & L054 --> L055
  L024 & L030 & L051 & L054 --> L056
  L024 & L025 & L040 & L051 & L055 & L056 --> L057
  L019 & L020 --> L058
  L058 --> L059
  L058 & L059 --> L060
  L058 & L059 & L060 --> L061
  L058 & L061 --> L062
  L024 & L058 --> L063
  L058 & L063 --> L064
  L064 --> L065
  L064 --> L066
  L064 & L066 --> L067
  L067 --> L068
  L064 & L068 --> L069
  L068 --> L070
  L067 --> L071
  L067 --> L072
  L072 --> L073
  L072 --> L074
  L072 --> L075
  L074 --> L076
  L074 --> L077
  L074 --> L078
  L074 & L078 --> L079
  L074 & L078 --> L080
  L074 & L078 --> L081
  L074 & L078 --> L082
  L074 --> L083
  L074 --> L084
  L084 & L085 --> L086
  L084 --> L087
  L084 --> L088
  L084 --> L089
  L084 --> L090
  L084 & L090 --> L091
  L084 & L090 & L091 --> L092
  L091 & L092 --> L093
  L084 & L091 & L092 --> L094
  L092 & L093 & L094 --> L095
  L084 & L091 & L092 & L094 --> L096
  L094 & L095 & L096 --> L097
  L094 & L096 --> L098
  L084 & L098 --> L099
  L074 & L078 --> L100
  L100 --> L101
  L100 --> L102
  L100 --> L103
  L100 --> L104
  L100 & L104 --> L105
  L074 & L104 --> L106
  L106 --> L107
  L107 --> L108
  L107 & L108 --> L109
  L107 & L108 --> L110
  L107 & L108 --> L111
  L107 & L111 --> L112
  L107 & L111 --> L113
  L107 & L111 --> L114
  L107 & L111 --> L115
  L113 --> L116
  L117 --> L118
  L118 --> L119
  L107 & L108 & L111 & L119 --> L120
  L118 --> L121
  L121 --> L122
  L107 & L108 & L122 --> L123
  L108 & L122 & L123 --> L124
  L108 & L122 & L124 --> L125
  L058 & L063 & L067 & L125 --> L126
  L058 & L060 & L063 & L064 --> L127
  L058 & L064 & L066 & L127 --> L128
  L063 & L064 & L067 & L127 --> L129
  L019 & L058 & L063 --> L130
  L129 & L130 --> L131
  L129 --> L133
```
