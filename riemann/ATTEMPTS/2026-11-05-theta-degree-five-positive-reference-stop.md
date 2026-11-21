# Actual two-node degree-five positive-reference stop — step551

The canonical finite result is
[L808](../lemmas/L808-actual-two-node-degree-five-reference-nonreal-roots.md),
with complete rational evidence in
`scripts/theta-gauss/reference-roots-certificate-551.json`.

WHY IT FAILS: The actual two-node reference Q_(2,5) has a nonreal
conjugate pair, certified in disks of radius1/100 centered at
26.150079 +/- 18.380803i. It therefore cannot meet the proposed
five-simple-positive-root premise for a real-reference signed barrier.
The other three roots are simple and positive. This stops this exact
reference-hyperbolicity premise independently of the earlier cubic
common-interlacing obstruction. Known actual P_5 hyperbolicity and RH
are unaffected. A changed reference or a compensation mechanism able
to handle nonreal reference roots needs a specific new target and source
coverage; relabeling the existing positive-root premise is insufficient.
Inherited L805/L778 evaluator/backend qualifications remain. Step553
independently reproduces the finite certificate: 161 checks PASS,
no defect found. The full audit is recorded in L808 and
`scripts/theta-gauss/reference-audit-certificate-553.json`.
