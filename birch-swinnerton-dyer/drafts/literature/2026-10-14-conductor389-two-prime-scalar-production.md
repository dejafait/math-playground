# Bounded conductor-389 two-prime scalar production — source review

TARGET: Assess source coverage for the single depth-one Kurihara-scalar computation on y^2+y=x^3+x^2-2x at p=7 using L032 and the lexicographically first Kim P_1 pair ell_1<ell_2<=500 with ell_1 ell_2<=100000, with a stop if no eligible pair exists.
CHECKED: 2026-10-14
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Targeted exact-model/Kurihara/p=7 searches located Kim's older primary numerical example and the author-cited Ghitza repository; read L030's arithmetic/presentation statement, L032's complete normalization/path/denominator argument and audit conclusion, L063's scalar premises/proof, relevant production/audit assessments, histories 220--223 and ATTEMPTS/021/029--031. No exact p=7 capped result was located; no absence or novelty claim follows.
SOURCE_EVIDENCE: Directly inspected Kim's publisher-hosted author text dated 2025-05-12, Sections 1.2.2 and 1.4.1--1.4.3, printed pp. 3 and 5, and Theorem 1.8 with its computational discussion, p. 6; inspected arXiv:2203.12159v3, dated April 7, 2022 internally, Section 8(1), printed p. 48, for the exact-model p=5 example. Reused L032's audited total-period calibration and Stein weight-two Propositions 3.10/3.11/Theorem 3.13 coverage; read the Ghitza repository README, not its implementation body.
COMPARISON: Kim defines the exact finite sum and depth-one reduction, and already reports a nonzero two-prime residue on this model at p=5. L032 supplies the matching p=7-integral full-relative symbol map. The p=7 capped instance and its complete certificate are uncomputed here; the next work is known-algorithm reproduction with exact replay, not a new scalar formula or rank theorem.
GAP: Produce and independently replay the eligible-prime search, fixed primitive-root/log tables and every term of the one selected sum; absence of a pair or a zero residue stops the schedule. All unsupplied L026 hypotheses and successful classical localization remain separate.
REASON: Primary definitions and existing audited symbol evidence now cover the bounded implementation and its explicit orientation/period comparison; approve only the covered computation below, without re-proving Kim or deriving a new lemma in this literature turn.
SCOPE: E=[0,1,1,-2,0], conductor 389, p=7, m=1, audited L030/L032 full-relative inputs, exactly the lexicographically first distinct Kim P_1 prime pair ell_1<ell_2<=500 with product<=100000. Certify the complete capped selection, fixed generators and all unit-residue summands including zero weights; no enlarged cap, extra scalar or stronger eligibility is covered.
COVERED_TARGET: Compute and independently replay the single depth-one Kurihara scalar for y^2+y=x^3+x^2-2x at p=7 from L032 at the lexicographically first Kim P_1 pair ell_1<ell_2<=500 with ell_1 ell_2<=100000, stopping if no eligible pair exists or after that one residue.
LITERATURE_REASON: The new target requires an essential explicit comparison of Kim's oriented plus-symbol definition with L032's full-relative table, together with precise eligibility and complete finite-sum certificate coverage.

This completes the saved literature-only action. No prime, trace, root,
logarithm, cusp value at the proposed index or scalar is computed here.
The earlier pending proposal is preserved by the unchanged TARGET and
its cap/stop conditions. L063's completed audit is unaffected.

## Source comparison and exact conventions

The governing primary source is Chan-Ho Kim, *The structure of Selmer
groups and the Iwasawa main conjecture for elliptic curves*, author text
dated May 12, 2025, [Sections 1.2.2 and 1.4](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf#page=6).
Section 1.2.2 (printed p. 3) specifies primes coprime to N_E p with
ell=1 and a_ell=ell+1 modulo p^m, and the sum ideal I_N. Section 1.4.3
(p. 5) explicitly permits reduction modulo p^m at N in N_m.
Section 1.4.2 fixes a primitive root eta_ell and the exponent log modulo
ell-1. At m=1 these exponents are reduced modulo 7. Eligibility and
the actual I_N convention must be certified, not replaced by a software
Kolyvagin-prime filter with additional or missing conditions.

Section 1.4.1's defining identity is
\[
2\pi\int_0^\infty f(r+iy)\,dy
 =[r]^+\Omega_E^+ + i[r]^-\Omega_E^-.
\]
Its Omega_E^+ is the total real period of a global minimal model. Compare
L032's I({alpha,beta})=Re(2 pi i integral_alpha^beta f(z) dz) and
F=I/Omega(E)=-phi. Along the path from infinity down to r, z=r+iy
runs from y=infinity to zero, so dz=i dy gives
2 pi i integral_infinity^r f(z) dz=2 pi integral_0^infinity f(r+iy)dy.
Taking real parts in the defining source identity therefore identifies
the entry [r]^+ with F({infinity,r}) directly. This is a comparison of
existing definitions, not a new lemma. It introduces neither reversal
nor averaging nor a connected-component period. L032's audited image
(1/2)Z makes every entry reducible modulo seven; use the inverse of its
actual rational denominator. The scale F=-phi must be retained.

Thus the covered evaluation is exactly Kim's sum
\[
d_1=\sum_{1\le a<N,\ (a,N)=1}
 F(\{\infty,a/N\})\,
 (\log_{\eta_{\ell_1}}a\bmod7)
 (\log_{\eta_{\ell_2}}a\bmod7)\quad\text{in }\mathbf F_7.
\]
No half-plus projection or finite Euler-factor correction is inserted.
The assessment imports this definition, not a theorem asserting its
nonvanishing. Theorem 1.8 (p. 6) and the prior L063 assessment cover only
the later conditional structural use; their hypotheses are not certified
by this source review.

## Duplicates and implementation coverage

Kim's [arXiv:2203.12159v3, Section 8(1), printed p. 48](https://arxiv.org/pdf/2203.12159v3#page=48)
already reports a nonzero residue at 41*61 for this exact equation at
p=5. That is an inspected overlap, not the requested p=7 value. The older
version has different theorem numbering; use the 2025 text for conventions
and structural citations. This overlap and Kim's computational discussion
identify the method as established. A new local p=7 replay would establish
an instance certificate, not progress beyond known methods.

The author-cited [Ghitza repository README](https://github.com/aghitza/kurihara_numbers)
describes Sage computation and a different example. Its code body was not
successfully exposed by the web views; a direct shell retrieval failed
with DNS exit 6. It is a nonessential implementation lead, not inspected
normalization or replay evidence. No cached Sage result is used. Searches
also returned third-party purported BSD solutions; their snippets were
not inspected theorem evidence and support no decision here. An incidental
arXiv:2203.12157 lookup identified a different paper and is unused.

Reuse L032's complete oriented integral path and calibration coverage,
including its full generator table and all relations; no new modular-symbol
theorem is required. The source/path reduction inputs are Stein, online
v0.1, [weight-two Propositions 3.10/3.11 and Theorem 3.13](https://wstein.org/books/modform/modform/weight_two.html),
already assessed and applied in L030/L032. The examined local independent
checker `scripts/quadratic-seven/verify_certificate.py`, lines 120--175,
provides a reusable certificate pattern, not verification of any proposed
new paths. A new implementation is justified by this exact capped target,
the already calibrated table and the need for complete independent evidence.
Reproving Kim or inferring universal correctness of prior software is not
justified.

The local search checked the specific production/audit assessments and
histories 220--223 rather than sibling notebooks. ATTEMPTS/021 retains the
failure of primitivity alone to eliminate the finite quotient. ATTEMPTS/029
parks an unrelated persistent CM source blocker; ATTEMPTS/030--031 preserve
the separate rational-membership/localization failures. None gives the
present residue or forbids a fixed test. L023's conditional existential
selection is not this independently computed scalar.

## Required certificate for the covered next attempt

1. Bind the actual L030 relative presentation and audited L032 calibration
   evidence without modifying them. Record E, N_E=389, p=7, m=1, the caps
   and selection order. Use exact integers and reduced rationals throughout.
2. Certify primality/compositeness sufficiently to cover every possible
   candidate ell<=500 with ell=1 mod7, exclude divisors of 389*7 and count
   the exact displayed model over every remaining candidate field. Retain
   complete finite count evidence and a_ell=ell+1-#E(F_ell). An independent
   replay can compare direct y-equation enumeration with root-count tables.
   Certify the sorted eligible list, all pair-cap comparisons needed for
   lexicographic minimality and absence of a pair when applicable. No count
   or pair is supplied by this assessment.
3. At the selected pair fix deterministic primitive roots (the least
   positive primitive roots are covered), and save all powers for exponents
   0,...,ell-2 as a permutation of the nonzero residues. Independently check
   every power, invert that table and check each exponent against its residue
   before reducing modulo seven. If least roots are chosen, certify failure
   of each smaller positive candidate. No generator-change heuristic is needed.
4. Enumerate the full unit set 1<=a<N and certify its size
   (ell_1-1)(ell_2-1). For every term, including zero log weights and zero
   symbols, save a complete oriented path infinity to a/N, its determinant-one
   segment lifts, Gamma_0(389) reductions, raw generator vector, full quotient
   coordinates, exact F value, both log residues and product modulo seven.
   Factoring the finite sum for efficiency is permissible only if the complete
   uncombined term accounting remains available for independent replay.
5. A separate verifier must import no builder. Verify path endpoints and
   telescoping, every segment determinant and exact coset-reduction matrix,
   full quotient reconstruction and agreement of evaluation through all
   generator values and through the quotient functional. Recompute the
   entire unit set, both logarithms, each rational reduction and the total.
   Reject missing/duplicate terms, ineligible pairs and altered arithmetic.
   Save full certificates/reports under an appropriate new notebook script
   subdirectory; print only residue, actual/required caps, counts, failures
   and paths. Inspect complete load-bearing evidence, not previews alone.

These are finite instance verification obligations within assessed known
methods; no new bound or theorem is proposed. Existing independently known
points/rank must not enter pair selection, guess a residue or replace replay.

## Relevance and stopping test

The main gap remains rank E(Q)=m(E) for arbitrary m(E)>=2. The one
intermediate target is the COVERED_TARGET. Its downstream use is testing
actual scalar production independently of an assumed finite length: a
fully certified nonzero residue would supply v=0 for L063 only after all
its L026 premises are separately supplied. It supplies no successful
class for L062 or strict rational Kummer direction. A zero residue supplies
no exponent certificate; no eligible pair under the caps supplies no
global nonexistence statement. Stop after this one pair regardless of
the residue, or immediately upon certified absence of a pair. Do not
continue to another pair, depth or cap within this attempt.

Coverage is ready for that bounded mathematical implementation/replay,
not for a new rank theorem. All L026 residual-surjectivity, local-torsion,
Manin/Tamagawa, residual-family, central-value/sign and coefficient premises
remain subject to their separate evidence; L033's existing coefficient
certificate is not enlarged. L061/L062 enter only a later supplied-class
application. Uniform production, rational membership and arbitrary
complex-order comparison remain unresolved. No cross-notebook input is used.

Queries on 2026-10-14 included `"389a1" "Kurihara" "7"`,
`"Kurihara numbers" "389"`, the exact Kim title with `"389"`,
and `"Kim" "389.a1" "Kurihara" "7"`. A failed or noisy search is
not evidence of absence. Full matching and supporting Mathlib coverage
for this finite computation are not checked; unknown coverage is not absence.
