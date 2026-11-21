# Local count: effective off-axis attempt2114

Completed working record. The approved target and SPECIALIZE assessment
remain exactly those in `drafts/literature/2026-11-21-local-heat-count-review-2111.md`.
Main gap: L030-L032/C032a actual-Xi mixed positivity. Intermediate test:
C488b's sufficient comparison |H_t/B_t-1|<=0.99 for x>=29399,
3<=y<=4, 0<t<=1/5. Its possible use is completion of constant100
local counts and, later, smaller C488a transport costs. Reality,
overlap and mixed signs remain separate. C488b is not independently audited.

Reused the supplied assessment; read C488b and its exact failed global
bridge (14), C488a's global-count/product proof, and the October30
explicit-source qualification. The source's printed y<=1 constants
cannot be copied to this band. Inspecting the same primary proof for
constant extraction is mathematical work under ready coverage, not
another literature comparison. No new source theorem or lemma has
yet been established.

Bounded attempt: follow the off-axis proof and expose numerical errors
on the required domain. Continue only with a complete uniform estimate;
otherwise record a specific failed estimate or remaining quantified
term, not sample values or an arbitrary asymptotic onset. Preserve all
earlier unfinished work. No supervisor state or shared infrastructure
is modified.

Partial calculation saved before write-up. Put T=x/2, b=sqrt(T/(2pi)),
T'=T+pi*t/8, a=sqrt(T'/(2pi)), N=floor(a), so b>48. For the two
real parts sigma in[-3/2,5/2], use Polymath6.2 directly, not6.3's
restricted conclusion: choose K=1 for u>=0 and K=ceil(-u)+2 for u<0.
The coefficient-plus-remainder magnitude admits the envelopes
9^u/[4(a-1)] (u>=0) and (16/a)exp(u^2/2) (u<0).
Taylor expansion and the stated Stirling error give the prefactor
exp((u^2+1)/(T-3)); retaining1 here avoids copying the smaller
constant in the printed6.3 derivation. Gaussian integration should
give |R_t,N(sigma+iT)|<40|M_0(iT')|. Need check all scalar bounds.

Proposed total: principal n>=2 sum<2/3, reflected main sum<1/8,
r-term errors<1/500, two normalized remainders<5/72. Their sum is
971/1125<9/10, now checked exactly. The completed proof is canonical
in `lemmas/C488c-effective-off-axis-local-heat-count.md`; it includes
all-height scalar monotonicity, the gamma-factor ratio, negative-u
coefficient envelope and Gaussian integrability. The scalar certificate
`scripts/heat/local-count-off-axis-2114.json` passes33/33 checks, with
the full selected checks inspected. No finite sampling was used.

The new proof meets C488b's sufficient comparison and hence the full
saved count target, but both need a separate conceptual audit. This is
local quantitative reproduction of the published method. It is not
progress beyond the source's order of magnitude and supplies no mixed
sign. Continue that same target under the unchanged ready assessment;
do not conduct another source-comparison turn without a specific new
coverage gap. A central creative continuation was not justified by
this constant-extraction attempt; the immediate essential task is the
analytic audit, not an invented mechanism to fill a scheduling slot.
