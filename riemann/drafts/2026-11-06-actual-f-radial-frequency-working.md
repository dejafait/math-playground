# Radial-frequency test: working checkpoint

6 November 2026. Approved target and reused source scope:
`drafts/literature/2026-11-06-actual-f-radial-frequency-isolation.md`.
No hypothesis of L872 is changed. The main gap remains
L030-L032/C032a; the intermediate target is isolation of one arbitrary
nonzero C0 forcing profile. Period, radial means, graph realization
and Xi signs remain independent gaps. L018, L847, C868a/C868b and
audited L871 are inputs; L872's unaudited moving error is a contrast,
not an estimate to assume. No cross-notebook input is used.

Unfinished operational test: fix a second angular index b != 0.
The k-th first-angle coefficient is U_(k,b)(k x1+b x2), bounded
uniformly by H. These coefficients define a tempered distribution
in the two radial variables and first angle, without transforming
q,r or the unrestricted zero mode. Its radial spectral lines have
direction (k,b). A compact radial window away from the second
frequency zero can meet only finitely many such lines, and a smaller
window should isolate a selected k. This requires a full proof of
distributional convergence and identification with the classical
angular projection, to be written canonically if valid.

Crucial unresolved operation: localization in both radial variables
convolves normally to x1=lambda_j and need not preserve its trace at
y1=pi. A compactly supported smooth scalar function vanishing on
all actual zero radii will test that operation; it is not a proposed
actual-F triple. Filtering x2 alone leaves x1 fixed but retains all
k. It also requires checking the angular restriction after radial
convolution, rather than assuming these commute. Continue only with
valid trace-compatible isolation or a precise new operation-level
obstruction; otherwise park this spectral mechanism. No script or
numerical experiment is needed for this test.

## Completed bounded test

The original checkpoint above is retained. The complete calculations
and precise citations now live in L873. The reconstruction and a
nonzero compact bandpass window were justified, and full radial
localization isolates one index exactly. Its normal convolution
does not preserve the zero-line trace class: the smooth diagnostic
has localized trace value 1 where preservation requires 0. It is
not a full actual-F example and does not decide rigidity. Tangential
filtering alone has no index-selecting factor. The spectral mechanism
is parked at this specific trace-preservation obligation, not at
L872's already recorded moving-limit error. No mathematical script
or numerical certificate was needed.
