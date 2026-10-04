# Residue-20 predecessor application: calculation checkpoint

The ready IMPORT target is the least nonconvergent residue-20 restriction,
not a new return rank. The main gap remains universal convergence after
arrival at residue 20. The proposed intermediate input restricts a
conditional least bad root to two possible 3-adic valuations; its use is
to reduce the domain of a subsequent ancestor or termination argument.

The cited guard is y=236 modulo 243. Write y=243k+236 with k>=0.
The predecessor c(y)=(8y-7)/9=216k+209 is positive, congruent to 20
modulo 27, and smaller than y by 27k+27. Its exact shortcut path is

    216k+209 -> 324k+314 -> 162k+157 -> 243k+236.

The first and third input states are odd; the second is even. Thus
these are actual shortcut steps for every k, rather than just a formal
affine identity. Also c(y)+7=8(y+7)/9 lowers v_3(y+7) by exactly two.

For a fixed least bad residue-20 root n, v_3(n+7)>=5 would give this
smaller bad root c(n). If c(n) reached 1 before the third step, all
subsequent states would still be in {1,2}, since T(1)=2 and T(2)=1;
therefore convergence transfers in either direction along the path.
Minimality rules out the case >=5. Membership in residue 20 already
gives v_3(n+7)>=3, so the remaining possibilities are 3 and 4.

The all-parameter parity, positivity, residue and strict-size checks
succeed. This imports the inspected source restriction and supplies
the local applicability argument; it is not progress beyond that source.
The achieved threshold excludes only valuations >=5. The required
global threshold is convergence, or eventual descent, for every root
in the infinite residual class. No forward decrease from n is proved.

L013 supplies nonemptiness of the bad residue-20 set if any bad positive
start exists: its terminal hit cannot be 1 or 2. The actual root is
never replaced by a larger returned state. A later return y>n followed
by c(y)<y would not justify comparison with n, as already screened in
Attempt 010.

The closest source is Sodelin, node AB-CORE-RESIDUE-OBSTRUCTION-001,
[section 6, raw lines 204–239](https://raw.githubusercontent.com/Sodelin/Collatz-Conjecture-Work/main/proof-search/routes/AB_ternary_normalized_core_residue_obstruction.md),
read in the saved assessment on 2026-10-03. Its exact predecessor
formula and valuation reduction are imported. No general inverse-word
theorem or new literature search is needed for these guard checks.
