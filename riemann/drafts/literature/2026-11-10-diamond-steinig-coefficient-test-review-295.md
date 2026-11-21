# Growing-order arithmetic decomposition: coefficient overhead test

TARGET: Test whether the exact unmerged Diamond-Steinig coefficient mass M_n is subexponential at order nu=n, retaining both partition families and all factorial weights, before proposing a growing-order estimate for L984(H).
CHECKED: 2026-11-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step295 searched exact Diamond-Steinig coefficient/norm and Laguerre combinations; compared the fixed-order Selberg stop, reviews231/245/278 and the new higher-uniformity source. No inspected statement decides this exact root-rate question; no novelty inference.
SOURCE_EVIDENCE: Ramaré, On Bombieri's asymptotic sieve, author preprint28 October2009, Section2/(12)-(18)/Lemma4, pp8-9; Lemmas5-7 with complete proofs, pp10-11; Lemma9 factorial estimate. Exact finite formulas and the exponential upper bound were inspected before this nomination; primary citation below.
COMPARISON: The normalized decomposition is known. Lemma7 gives an exponential upper bound, not the exact growth or a lower bound. Only quantitative specialization of that explicit arithmetic identity is proposed; no prime-correlation theorem or new identity is needed or claimed.
GAP: Determine limsup log(max(1,M_n))/n, or bounds decisive for zero versus positive rate. No answer, asymptotic, arithmetic weighted bound or RH consequence is established here.
REASON: Growing order is a materially different input from the stopped fixed-order coarse remainder. Its exact overhead is an independently testable prerequisite to one termwise use. This new ready assessment requires separate next-turn approval before mathematics, not a new source search.
SCOPE: Integers nu>=1; exactly the unmerged mass on the left of Ramaré Lemma7. Finite identities and elementary factorial bounds only. No optimization over representations, sieve theorem application, actual prime estimate, zero sum, new zero-free region or RH assumption.

## Exact primary input and observable

Use O. Ramaré, *On Bombieri's asymptotic sieve*,
[author preprint28 October2009](https://ramare-olivier.github.io/Maths/V12BombieriSieve.pdf#page=8),
Section2/(12)-(18)/Lemma4 and Lemmas5-7, printed pp8-11.
Lambda^(t)(m)=Lambda(m)*(log m)^(t-1)/(t-1)! in this source;
do not confuse it with the higher-order function mu*(log)^t.

K_nu contains nonnegative integer vectors k=(k_1,...,k_(2nu)) with

    sum_j j*k_j=2nu,  1<=r=sum_j k_j<=nu.

As in(14), put

    c(k)=(-1)^(r-1)*(r-1)!/prod_j k_j!,
    w(k)=prod_j (j!)^(-k_j).

H_nu consists of ORDERED pairs (k',k'') of nonnegative integer
vectors of length nu, each of weighted sum nu, whose lengths
r'=sum k'_j, r''=sum k''_j obey r'+r''<=nu. Both lengths
are positive; H_1 is empty. As in(16), use

    cbar(k',k'')=c(k')*c(k''),
    wbar(k',k'')=w(k')*w(k''),

with the same c,w formulas on the shorter vectors. Define

    M_nu=2nu*sum_(k in K_nu) |c(k)*w(k)|
          +nu^2*sum_((k',k'') in H_nu) |cbar*wbar|.

This is the UNMERGED coefficient mass. Take absolute values before
combining families or identifying equal convolution factors; do not
replace it by the norm of collected a(ell) in(18). Lemma7 gives
M_nu<=(nu+2)*2^(nu-1). Its complete proof uses Lemma5's
length-resolved count and Lemma6's factorial weight bound. Import
these known inputs; do not reprove the general identity or sieve.

## Bounded test and decision

Set nu=n to match the proposed growing-degree scale and decide

    limsup_(n->infinity) log(max(1,M_n))/n = 0.

A rigorous strictly positive lower rate rejects the claim; a sharp
asymptotic is unnecessary. Alternatively prove the every-epsilon
upper bound if it holds. Keep both families, all factorial weights
and length restrictions. Exact finite rational values may guide a
proof but never decide this asymptotic question. No parameter sweep
or replacement representation is part of this test. The known upper
bound alone leaves the answer unresolved.

Ramaré Lemma9 supplies the standard two-sided factorial estimate
for all positive integers. Optional tools are
[DLMF5.11.1](https://dlmf.nist.gov/5.11.E1) on positive real
arguments and [DLMF26.8(i)-(ii)](https://dlmf.nist.gov/26.8)
for partition definitions/generating functions. No uninspected
uniform saddle theorem is approved or required for elementary bounds.
If a script is useful, save exact evidence and print only decisive
bounds, failures and paths. Finite samples are not proof.

Positive rate stops automatic subexponential overhead for this
particular termwise representation at linear order. It does not
exclude merged identities, correlation-retaining bounds or Selberg
methods. Zero rate only warrants formulating and separately assessing
a weighted arithmetic-error interface. Do not derive that interface
in the same test. If bounds are inconclusive, save the exact unresolved
inequality and require a refined mechanism before repeating the test.

## Relevance and independent gaps

The main unpaid input is L984(H); L981/L982 fix the actual cutoff
and compensation. Higher-order decomposition might replace a
fixed-order absolute estimate by a growing-order arithmetic identity.
Its coefficient costs must be understood before assigning termwise
subexponential error budgets. This is the sole downstream use of
this precheck, not an established route to (H). Favorable overhead
does not estimate factor norms or signed bilinear terms, reconstruct
the exact Laguerre average, pay endpoints/complements, or control
regulators and infinite zeros. Those gaps remain explicit.

Preserve the fixed-order Selberg stop, centered-Vaughan stop244,
transport stop279, spectral stops284/285 and audited L997. The new
input is the explicit order-dependent decomposition; no old error
has merely been renamed. L993 supplies conditioning only. No
cross-notebook input, simplicity or arithmetic sign is assumed.
Full matching Mathlib coverage is unchecked and unknown.

Expected task: calculation, standard/high, REPRODUCTION under
SPECIALIZE. This arithmetic-decomposition diagnostic is neither a
new prime estimate nor a claim of mathematics beyond checked sources.
