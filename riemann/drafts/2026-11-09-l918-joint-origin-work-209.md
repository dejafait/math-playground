# Step209 working checkpoint: one joint-row origin test

Gate: reuse the supplied EXPLORE assessment
`drafts/literature/2026-11-09-l918-origin-joint-elimination-test.md`.
The main gap remains L030-L032/C032a. The sole attempt is its exact
joint-row origin test; the actual-theta sign is not assumed or claimed.

The interface check of L918(5) agrees with L874/L917: in x=z^2,
g=1+sum (-1)^k y_k x^k/(2k)!, log g=-sum S_k x^k/k,
and 1/g=sum a_k x^k. T_n=a_n-a_(n-1)u^2/2+O(u^4), so
W_*/u^2 tends to minus the stipulated J. The density correction is
O(u^12), because its score is bounded at the origin.

Joint reduction: put p=c0/c2, q=c1/c2, h=S1, b=S2, d=S3.
The three rows, in order, give
S4=-pb-qd, S5=pqb+(q^2-p)d,
S6=(p^2-pq^2)b+(2pq-q^3)d.
H2=B^T A B, where A=[[b,d],[d,-pb-qd]] and
B=[[1,0,-p],[0,1,-q]]. This retains singular cases and divides
by neither c0, c1 nor a minor. Unit normalization gives
c2^2=1/(1+p^2+q^2).

One proposed exact relaxed witness, not yet certified at this checkpoint:
h=1, b=d=1/1000000, p=1, q=-3, c=(1,-3,1)/sqrt(11).
Thus (S2,...,S6)=(1,1,2,5,13)/1000000 and H2 is a positive
multiple of [[1,1,2],[1,2,5],[2,5,13]], with rank two.
Recover y0,...,y6 by exp(-sum S_k x^k/k) modulo x^7.
Check every principal minor of (y_(i+j))_0^3 and
(y_(i+j+1))_0^2, all H2 principal minors and null rows, unit
normalization, and J exactly. No parameter or support-family sweep
is authorized. No representing measure will be claimed.

If all constraints hold and J<0, this is only an obstruction to the
fixed finite relaxation: equality with actual theta moments, the
lambda tilt relations, full support and all higher moments remain
unverified/omitted. If no sign/witness is certified, preserve the
unsigned reduction and stop the mechanism. Actual contact existence,
the compact residual, flux, initialization/equality, higher degrees
and global continuation remain open. This note is unfinished work,
not a canonical result or a completed outcome.

Completion of this checkpoint: the one proposed tuple passes every
constraint and has J<-7/100. The full proof, exact moments/minors,
qualifications and reproduction command are now canonical in L921;
the complete certificate is `scripts/heat/l918-joint-origin-relaxation-209.json`.
The earlier text records reasoning before that calculation. No
unfinished search or automatic second witness attempt remains.
