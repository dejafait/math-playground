# Distance-shell constraints — primary source applicability

Hyun Kwang Kim and Phan Thanh Toan,
[Improved Semidefinite Programming Bound on Sizes of Codes](https://arxiv.org/pdf/1212.3467v1),
arXiv:1212.3467v1, 14 December 2012, III.C.3, printed pp. 11–12:
definitions (46)–(50), Proposition 15 (51)–(52), Lemma 16 (53)–(54),
Theorem 17 (55), and its complete proof (56)–(59). Inspected 2026-10-06.
This is a standard source input and applicability review, not a new lemma.

## Hypotheses

C is a nonempty binary length-n, weight-w code with minimum distance
at least an even integer d, and d<2w<=n. Put v=n-w and
H={d/2,...,w}. For i in H, V_i consists of binary vectors with i ones
in each of the coordinate blocks of lengths w and v. For distinct i,j,
m_ij is the maximum distance between a vector of V_i and one of V_j.
Choose positive integers Q_i>=T(i,w,i,v,d), where T is the maximum
size of a doubly constant-weight code with the displayed weights and
lengths. Set S_(2i)(X)={Y in C: dist(X,Y)=2i}; B_(2i) is its average
cardinality over X in C. In foundations/04's normalization,
B_(2i)=binomial(w,i)binomial(v,i)p_i by source equation (40).

## Conclusion

Proposition 15 gives, with u=i+j,

\[
m_{ij}=\min(u,2w-u)+\min(u,2v-u).
\]

Lemma 16 bounds each shell cardinality by Q_i. Theorem 17 requires a
nonempty H_1 subset of H with m_ij<d for every distinct pair in H_1.
Its conclusion is sum_(i in H_1) B_(2i)/Q_i<=1. Singleton H_1 is allowed,
but gives only Lemma 16's individual shell bound.

## Proof

Import the cited statements and Theorem 17's proof (56)–(59); no reproof
is needed. Its proof moves an anchor X to (1^w,0^v), translates other
codewords by X, uses m_ij<d to contradict two occupied distinct shells,
then uses Lemma 16 and averages over anchors. The empty-shell and
single-occupied-shell cases are included. Lemma 16's proof (54) invokes
Proposition 1 and block complementation. Proposition 15 supplies the
explicit formula but says only that its proof is straightforward; no
longer source proof is claimed to have been inspected.

For L022's unchanged instance n=1024,w=68,v=956,d=10, all code hypotheses
hold. Here H={5,...,68}; for distinct i,j in H, 11<=u<=135<956.
Direct substitution in (51) gives m_ij=2u>=22 when u<68, and
m_ij=136 when u>=68. Thus there is no eligible two-element H_1.
Theorem 17 cannot impose a coupled-shell constraint at these parameters,
independently of the chosen Q_i or the values of the assignment. This
does not assert that individual shell bounds pass or are redundant.

The adjacent Theorem 19 (70)–(72), printed p. 14, expressly requires
i+j>=v and m_ij=d. Its prerequisite already fails because u<=135<956;
no implementation of that alternative is justified. This agrees with
the source's alpha<=0 warning on printed p. 16, where alpha is defined
in (82). Only its statement-level prerequisite was used; its full proof
was not needed for this rejection.

These source substitutions change the choice of diagnostic, not the
assembled list-decoding argument. The 955–957 bracket, omitted SDP
blocks, exact packing coefficients and realization questions remain open.

## Mathlib

Full matching Theorem 17 and constant-weight distance-shell machinery:
**not checked**. No library absence or novelty claim is made.
