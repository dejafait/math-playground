# Actual theta exponent score: fixed fifth Jensen diagnostic1325

TARGET: Test whether the fifth Jensen polynomial of h(z)=d/dz log(K(-iz)/K(0)) has only real zeros, using certified actual-theta derivatives through order six, and use failure only to exclude derivative-LP exponent models matching that local jet.
CHECKED: 2026-11-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse completed source discovery1325 and its exact-name/score-potential/Jensen searches. Existing Xi-moment Jensen, heat-contact and scalar Stieltjes tests involve different objects. No matching fixed actual-kernel score test was located in those scoped records; no originality claim.
SOURCE_EVIDENCE: Craven--Csordas Pacific J.Math.136(2)(1989),241-260, (1.3)-(1.4) pp241-242 and (2.1)-(2.3) p242; Proposition2.1 and Lemma2.2/proof pp243-245 read. The sufficient exponent class is Branden--Chasse arXiv:1402.2795v2 Section5, Theorem5.4/Corollary5.5/Proposition5.6 with relevant proofs, extracted in discovery1325. Precise links and full qualifications are there.
COMPARISON: LP membership of an entire score implies real roots for each Jensen polynomial; only its fixed n=5 necessary condition is tested. Known theorems do not determine the actual K jet or prove its score belongs to LP. Certified differentiation and a rigorous root decision are the actual-law specialization; no reproof of the source theorem is needed.
GAP: The polynomial is uncomputed. Local analyticity, reality/parity and the logarithm branch must be justified before computing it. Global exponent continuation, all-order LP membership, actual approximation/convergence and all-degree Xi positivity remain unproved irrespective of a passing test.
REASON: This bounded discriminator is available after recovering the previously unread exponent criterion. A local failure could exclude every sufficient-class exponent model matching this jet; a pass establishes compatibility only at n=5. No automatic higher-degree campaign is proposed.
SCOPE: Nomination written in literature step1325; separate next-turn approval is required before invocation. Exactly n=5 at the origin for the actual L019 kernel, not Xi, its moments, an adjustable kernel or a heat deformation. No parameter sweep, global natural-boundary proof or RH conclusion.
COVERED_TARGET: Test whether the fifth Jensen polynomial of h(z)=d/dz log(K(-iz)/K(0)) has only real zeros, using certified actual-theta derivatives through order six, and use failure only to exclude derivative-LP exponent models matching that local jet.

## Object and source contract

K is exactly L019's full theta series. Near the origin use its complex
series germ and the logarithm branch with value zero at z=0. Set
G(z)=log(K(-iz)/K(0)), h=G', and a_k=h^(k)(0), 0<=k<=5.
The nominated polynomial in the source's derivative convention is

    J_5(h;X)=sum_(k=0)^5 binom(5,k) a_k X^k.

This defines the proposed test; no a_k or identity with Xi power sums
has been calculated. The logarithm is initially local only. Before
any root decision justify the complex series and its fixed-order
differentiation, K(0)>0, a nonzero neighborhood and the relevant real
symmetries from L016/L019 and the theta transformation. If a symmetry
is unproved, retain that gap rather than drop coefficients numerically.
No assumed zero location is allowed.

The standard necessity is Craven--Csordas (1.3)-(1.4),
[publisher PDF](https://msp.org/pjm/1989/136-2/pjm-v136-n2-p03-s.pdf).
It applies under a hypothetical entire LP extension of this same h;
it needs no positive-coefficient assumption. Formula (2.3) also fixes
the derivative shift. Avoid the separate positive-coefficient Turan
converse. The sufficient exponent theorem and its qualifications are
in [discovery1325](2026-11-17-actual-xi-sufficient-mechanism-discovery-1324.md),
first mechanism, not rederived here.

## Relevance and precise limits

The main gap is L030-L032/C032a actual mixed positivity in every degree.
A global applicable exponent construction could give zero location
through the known theorem and L020's transform. No such construction
is asserted. This fixed polynomial tests only a local necessary premise.

Failure excludes an entire LP score with these derivatives, including
exact jet-matching exponent models. It does not exclude real-axis,
weak, integral or transform approximations without separate closure
hypotheses. De Bruijn p221's complex-local universal-factor warning is
context, not an input or a license to infer those closure statements.
This is not proposed as another proof of that warning.

A pass supplies neither entire continuation nor the next Jensen
condition. Stop this fixed test and report what additional independent
construction, if any, warrants work; no default degree extension.
An inconclusive coefficient/root certification must remain inconclusive.
A floating root preview or rounded discriminant is not proof.

Continuation test: certify the actual coefficients with full series-tail
errors, then certify either that all roots, including multiplicities
and possible degree loss, are real, or that a nonreal pair exists.
An exact sign/root-count criterion with strict interval margins is
acceptable. Retain failed bounds. Any script must save its complete
certificate and print only the outcome, actual/required bounds,
failures and relative paths. No script has been written here.

Essential local inputs are L016/L019 for the full series and derivatives;
L020 supplies downstream relevance. L030/L032/C032a locate the goal,
not a positivity premise. C031e and its C031c/C030z boxes are not inputs.
The Xi-moment q-Pascal, heat-contact L874 and scalar Stieltjes stops
are contrasts, not transferred counterexamples. Entire continuation,
global class membership and every actual Xi sign remain unresolved.
No cross-notebook input or RH assumption is proposed.

After approval classify the calculation REPRODUCTION, standard/high.
It specializes known necessity and is not a creative mechanism or a
full audit of the sufficient theorem. A central creative attempt still
needs an independently specified actual construction. Mathlib matching
coverage is unchecked, not absent. This nomination establishes no
lemma, inequality, jet value, root result or approval.
