# Primitive eleven-adic correlated image — working attempt

Approved target and prior SPECIALIZE assessment:
`literature/2026-10-17-primitive-eleven-two-descent-image.md`.
Completed task type intended: proof_attempt; classification REPRODUCTION.

Main gap: positive primitive integer emptiness. The intermediate target
is the exact whole-fiber two-descent image at eleven, potentially supplying
a further primitive-point restriction alongside L084. Acceptance requires
uniform containment and exact simultaneous realizations, with all three
base factors and all embeddings. No global independence is assumed.

L044 confines every compatible primitive scalar to residues 4 or 10.
L042 puts the smooth root at x=5-s+s² modulo eleven and all other roots
at x=16+121Z with Z=1/(s-1) in the residue field. The entire cubic
and its full local Kummer images are fixed in L073; use X=4x and its
same roots alpha,beta,gamma, with beta-gamma of valuation 5/2 over Q11.

Initial calculation plan: lift alpha modulo 11³ and compare the cluster
X with c=(4-alpha)/2. If (X-c)/121 has fixed nonzero square character
on each of the two residue disks, that controls BOTH quadratic-root
components uniformly, even in the degree-ten field. The smooth point
is controlled separately by its residue. Realization must still use
L042's entire fiber, not independent local points. This was the saved
unfinished reasoning before calculation; the completed result follows.

Recorded failures checked: ATTEMPTS/033 concerns the unrestricted odd
class and does not settle this restricted set; ATTEMPTS/034–036 stop
specific affine unit lists, and 037 parks class arithmetic. Their
mechanisms are not reopened. The supplied completed source assessment
already compared these and the different isogeny in ATTEMPTS/014.

Completed: [L085](../lemmas/L085-primitive-eleven-two-descent-image.md)
contains the full proof and citations. Alpha=844 modulo 1331 makes the
cluster unit residues 9 and 2. Smooth and clustered factors give the same
square-class character at each scalar, and the new exact residue-ten
fiber realizes the second tuple. The exact restricted image has size two
versus sixteen unrestricted. All 26 arithmetic checks pass. No global
independence or dimension improvement is claimed; critical audit requires
the separately proposed source review.
