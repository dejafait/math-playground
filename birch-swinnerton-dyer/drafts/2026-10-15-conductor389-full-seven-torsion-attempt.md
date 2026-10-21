# Fixed full seven-torsion construction (work checkpoint)

Approved target: construct and independently verify the full nonzero
7-torsion algebra for y^2+y=x^3+x^2-2x as an arithmetic input to L066.
Prior coverage is SPECIALIZE in
`drafts/literature/2026-10-15-conductor389-full-seven-torsion-algebra.md`.
This is a known-algorithm reproduction, not a new descent theorem.

The main gap is arbitrary-curve rank equality when complex analytic
order is at least two. The intermediate target is the complete global
torsion algebra, potentially useful for L066 item 1. Functions, incidence
maps, embeddings/local factors, complete units/classes, local bounds,
Selmer dimension and successful localization remain independent inputs.
No L026 residual nonvanishing is assumed or produced by this calculation.

Plan: transport to X=36x+12, Y=216y+108; verify the substitution and
inverse before using the cited division-polynomial theorem. Retain the
48 standard monomials X^i,X^iY, i<24. Test t=Y+kX for 0<=k<=64,
stopping at the first complete invertible power matrix. Retain all
recurrence data, Bezout witnesses, full matrices, coordinate inverses
and modular factor evidence; independently reconstruct them without
importing the producer. Prime search is limited to primes<=200.
Failing either cap is a partial construction, not irreducibility failure
or impossibility of descent. Original evidence must survive bounded
corrupted-coefficient and missing-map tests.

Startup checks read L030's model/nonsingularity and the relevant L065/
L066 obligations; ATTEMPTS/032/033/034 are preserved. No completed local
algebra duplicate was found in the supplied assessment or targeted paths.
The system python lacks sympy/flint; exact standard-library arithmetic
was used. The preceding paragraphs preserve the initial work checkpoint.

## Completed bounded attempt

The canonical result and full proof are L067. The first parameter k=0
produced a faithful power basis; primes 2 and 3 failed squarefreeness,
and prime 5 supplied all degree-48 Rabin witnesses. Independent complete
replay passes 4852 checks, including both model substitutions, all
recurrence coefficients, both rational Bezout identities, both matrix
inverse products, 49 powers, every coordinate map, 96 generator products
and every finite-field witness. The two prescribed altered-evidence
tests reject at their intended checks, preserving original bytes.

This supplies one degree-48 field as the complete global torsion algebra,
which is local progress by known algorithms. It produces none of the
other L066 inputs and no mathematics beyond the sources assessed.
The initial producer trimmed a zero slot before appending the monic
term, giving a wrong degree-47 polynomial; the entire unverified draft
is preserved and excluded from proof. The corrected degree-48 certificate
passes independently. No cap was extended. A separate critical audit is
the proposed next target and requires its own literature approval.
