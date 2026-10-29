# Common-height overlap working record

Approved target: audit the common-height L465/L464 assembly for each
fixed c_0>1/2. The supplied SPECIALIZE assessment is reused unchanged.
The component statements and their coefficient-normalization passages
have been inspected; no component reproof or external import is needed.

Completed write-up: choose the absolute C>0 of L464 and the uniform
height onset T_A(c_0) of L465. With ell=log(t/(2π)), L=log(t+2),
set A=log(2π+2). For t≥2π and ell≥A, L≤ell+A≤2ell.
Thus ell≥8C ensures C L²≤ell³/2. Increase a single existential
height onset to impose these conditions and ell²≥c_0. Split at
2p=ell³; equality goes to L465, and every larger integer order
goes to L464. Check ceil(c_0 ell/2), floor(ell³/2) and the first
integer above the latter explicitly. Neither component divides by
the possibly vanishing central Xi value.

This is an assembly of source-stated mathematics, not a new sign
range beyond paper 41 v4 Theorem 1a. Its downstream use is the
unconditional eventual tail; fixed low orders, effective bounded-height
overlap and global mixed positivity remain open. The endpoint check
passes. The full proof and qualifications are canonical in C465a,
`lemmas/C465a-unconditional-common-height-xi-tail.md`.
