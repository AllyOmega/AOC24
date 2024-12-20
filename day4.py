#part 1:
#graphish problem. detect word XMAS in 8 directions. 
#BFS or DFS?

input = '''
XMXXMSSSMSXSXMMXSAMMXXSXMASMSSXXMAMXAMXSXMXSMAMMASXXASMMXMASXMSSXMMMXMXSXXSXMXXSAMXSXSXSAMXMSAMXMAXXXMXMAMSASXMSSXMSXSXXMAXXSSSMXMXMXMMAASXM
MSSMMAAXAMMSAAAXXAMSXMAMXMSMAMMXSAXMXMASAMASMAMMASXMAMAXXXMASAAAXMSMSMAMAMMAMAMMMMXMASMMXMXAMASXMAMMMMASMMSMMMMASAAXAAMMMMSMXAAMSAMSASMMMMAX
AAAXMMXMSMASXMMSMXMMASMAAMXMASAMMAXSAMASAMASXXSMASASMSMMMMASMMMMMMAAXMXSAMSAMASMASAMAMASMMMMSAMXMAXAASASAAXAAXMASMMMSMXAAXAAMSMMMAXMAXMAASMM
SSMMXSAAXMMSAXMAXAAXAMXXMSSSMSMAMAMXAMXXXMXSXMMMMSAMXAXXAMXAXXMAXMASMXASAXXMSAXXASAMAXAMXXAXMXXMSASXMMASMMSSMSMMSASAMXSSSSMSAAAXMMMMXMMSXSXA
XAAAAMMSMSXXMXAASXSMSMSMXXMAMXMASXSSMMXMAMAMMMAAMMAMMMXSSMSAMXSMSASMXXMSXMAAMAMMMSXMAMMSXSASASAMXASXAMAXMAAAAXXMSXMXMXMXMAXAMXSAXAAXAXAXAMXS
SXMMSXAXASXAMMMMSXMXMASXMMXMMSMAXXMAMAMXAMASASMSMXAMXMMAMASAMXSXMMXAXSXSAMXMMAMAAMXMASMAXAAMAMSMMXMMMMMSMMMSAMXAXMMMSXSASMMMSMMMSSSMMMMMAMSM
AAXAXMSMAMSMMAAMSMSAMMMAMAASASMASMSAMAMMASASASXMASMSMSAAMAMAMAMASXMMMAASXMAXSASMMXAXAMMMMMSMXMAXSASASAMXXSMMMSMMMAXAAASAXSAXXAAAMAMXSASMXMAS
SSMMSMAMSMSXMSMMSASXSXSAMSMMASASMMSASASMXMMXMMXMASAAAXAMMXSAMASMMMAXXMMMXSAMXXSAMSMMSSXXAAAMMSSMSASXMASMXMASAXAMSSMMMMMMMMXSSSMXSAMXSASXMSMS
XMAMAXMXXAMAMAMAMXMXXASAXAXMXMXASASAMASMSAMXXSSMMMMMMMAMXMSASXMMASMMSSMMMSMMMMMMMASMXAMSMSMSAMXAMAMAXAMMMMAMMMSAAXSASASASXMAMAAXMASXMMMMXSXS
SMASXSXASASAMAMXSSSSMASXMASMSMSAMXMAMXMASAMSXMAASAMSXXMMXASAMXMSAMAAXXAAAMAMMAAMXAXXMAXMAAXMAXMXMSMSMMMMAXMMSAAMXSMXSASAAMAMSXMMSXXAXAAXMSAS
XMAXMXAXSAMXXXMAMXAAXMMMXAAAAAXASMSSMXMXMAMXASAMMASMXSXMXMMAMAAMASMMSMSMXSAMXMMSMSSXSXMMSMSSSMXXAMAXMAXSAXMAMXSAMXXXMMMMMASXSMSXXMMMSMMMAMMM
SMSSSXSAMXMMSMSMXMSMMAAXXSXSMMSAMAMAXXXXSAMSAMASMXMMASAMXXMAMSSSMMAXAXAXXMMXSAMSAMAMXAXXMXAAXXAXMMSMMSAMXSMASAMAASAMSAMXXSMAXAMMXAAMAMXSMSMS
SAXAMAXAMAAASAAAAMAXMMXMMXMXAMXAMAMMMMMMSSXMAXAMAXAMMMMSAMSMXXMAMXMSXSMSMSAAXAMMAMMMSXMMXMMSMAMSMAMAAXMSAAXAMXSMMAMAAASXMMMMMSMMMSXSASMSAAAA
MMMAMMMSXSSMMSMSXSAMMSMMASXMSMSMSASXAXAXMXXSXMSSXSMXSXXXAXAMMMXAMAAXMSXAMMMSSMMSAMAMAAMSAMXAMAMXMAXMMSAMXSMMSAXASXXXSXMXXAAAAMAMAMXSAMAMSMMM
SSSSMMXMXMXAAMXMASAMSAMMAXXAAAAAXASXMSXSAMXMAXXAXXMASMSMMSMSAMMSSMMXAMSXSAMXAMAXXXASXMMAMMXXSXMAXMXSAMXMAMMXMASMMMSXMAMAXXSSMSAMSXMMSMMMMMMM
SAAXMMAMAXSSMSAXAMAMMAXMMSMSMMMSMSMMXAMMXAASMMMXMAMASAAAAAASMSAXAAAMMMMMSASMMMMSSMMXAXSMMSAMSAMAMSAMAMAXSXMAMAAXAAAMSXMASXAAMMMMAAMAMXXXAAAA
XMSMSMASMMMMASMMSSSMSSMSAAXXASAMXMAMMASMMSXSXAMXSXMAMXMSSXXMAMXSMMXSAAAASXMASXSAMMSSSMXAAMAMSAMSSMASXMSAMXSSSSSMXSAMXXSASMMMMAAMSSMAXASMSSSS
MXMAASMMMAASXMXXAAXMAAAMSSMSXMASAMAMSSMAAXAMMMXXMXMAXAXMAMXMXMXXXMASXSMXMMXAMXMASAXMMAMMMSMMMAMXAXAMMMMAMAMAAXXAMMMXXMMXMXSXSSMMAMMSMXMAMAMM
XAMMMSXAXSXSMMXMMMMMSMMMAMASXMAXXXXMXAMMXXASAXXAXMSAMSSMSAMXAMXMMMXSAMXAASMSSXSAMMSAXSMSAAAASAMXSMXXAXXXMAMMMMSXMAAMMMXAAXXAMXXMASAAMXMAMAMX
SASMAMMMMMASAMXMMXSAAXXMXMXMASXSMSMMSAMSSSSMAASMXMASMAAAMASMAMAAXMAMXSSMMMAXAAMXMXMMMXAMSSSMSAMXAAMSSSMMSXSXAXMAMXMMAXXMSMMMMAXSAAXASXSMMAXX
MASMMMAXAXAXXMXSXXMAMSAMMSXSAMAAAAAAXAMAAMMMXMAAAXAAXAAMMAMMAXASMXXMSMASMMMMMMMAXAASAMXMAMAXMXSMMXMAAAAAAASMMMMAMMSSXMXMAMAAXSMMXXXSAMXASMMS
AASAMMSXMAMSSMASMMMAXMASAAXMASMMSMMMMSMMSMSSSXMSMMMSAMMSXASXMSMXMAAMASAMXAXSMXSMMSXXMXSAMXXMSSMMXMMMSMMMMAMAMASXMAXMASMSMSSSXMAMAMSAXSAMXSAA
MASAMAXXXMAAAMAXAMXXXSAMMMMMMMXXXXXSAXAXMAAAMXMAXXXMAMAMMAMXAAAAMSSMAMMXMMMMAAXMAMMMMAMAXXMASXAXMXAAXMAMXASAXMAAASMMMMMAXAXXMXAMASAAMXXXAMMM
SASAMASASAMSSMASXMMSAMMMMASXMASMXMMMASAMXMMSMXSAXSMSAMASMMSMSMMMMAAMAMXSAMSSMMSMASAAMAMAMXASMMMMMSMMSASAMASASMMSMXAAAMMMMXMSMSSMXSMAAMMMXSAX
AAXAMXSAMMAAAMASAAAMXXXASASAMMAMAMAMMMMMMSMMMMMMSMASXSASAAAAAXAMMSSMSAAMAMAAXXXMAXMMSXSAMXSAXSAAXAAXMAXAAMMMMAAMASMMMSXXXAAXMAAXXMXMXAAMAMMS
MXSSSMMMMXMSXMASMMMSMMSXSASXMMMSXSXXXAXAAAAAMAAXAMMMAMAMMMMMMMMSAMMAMMXXMMSSMMAMSSMXAMMXSMMSXMASMMSMMAMXXSASXMMMAMMXAAMSMMXXMSSMXMASMMMSXSAS
XMMAAASAMXXAMMXXAMAXAAMXMAMAASXMAXMASMSMMXSMSXSXSSMMXMSMMSXXAAXMAXMXMMMSMAAAASMXAAMMAMSASXMXMSAMXAXXMSMMASAMXMAXSMSXMSAMXSAMMAAAASASMMMAAMAS
MMMMMSXMSASMSXSSSMAMSXSAMAMMMSAMXMXASAAMMMMASAMXMAMMMAXAAAMSSSSSMMAAAASAMXSSXMMXSMMSAMMMSASAMXMMMSMMMXAXAMXMSSXSAAXAMXXSAMASMSSSMXAMAASMMMAM
MASAMXMXSAMXAAXAMMXXMASASXSSSSMMMXMXSXXSAAMAMAMMAMASMMXMAMXAMXMASMXXSMSASMMMMASAMAXMAMAXXMMASMMAAAAAASAMXSAXAAMSMMSXMAXMASAMAXAAAMSMSMSAAMAS
SASMSAAAMASMMMMAMXMASAMXMAAXASXASAAMMXASMSMAMXMAMSAXSMAMXSMMMSMMMMAXXXSAMAAAXXMASMMMASMSSXSAMASMSSSMXMAMAXXSMXMXXASMMMXSAMXMMMMMXMMAXASMMSAS
MASXSMSXMSMMAXMXMASMMMSSMMMMMMMMSMXAAXMSXAMSMSXXAMXXMMMSMMASAMMXSMMMSAXMASXSSMMXXMASXAMXAMMMSXMMMAXMASMMSSMMXMXXMXXAXAAMASXAMAXMXMMSMMMXAMAS
MSMAMAMMXXASMSMXSMMXASAMXMXXAASXMMSMMMXMXMXMAMMSMMSMSAMAMMAMASXAXAAAMMMSXMAMMXSXMXMMXSASAMAXMAMSMMMSAMAAAAAMXSMMSASMMMMSMMMMSMSMXSAMXAXMMMAS
SAMXMXMMAMAMXXMAMAASMMMMSXMSSSSXAASAMSXMXXAMAMAAXMMASXXXSMXXAMMSSSMSSXXMASMXAASMXAAAMXMSASXXSAMXAAAMAMMMMSSMMMASXMAAXAAAXMAXAMAMXMASMMSSSMSS
AMMASXAMMSMSMSMSSSMXMASAMMMAMAMMMMSAAMAMSMMSSMSMSAMXMSMAMXSMXMMAXXMAMAMXMMXMMXSASMSSXSXSAMAASAMXSMSSMSSSMXXMAXSMAXSMMMSSSSSSSSSSXSAMAXAAAMAS
MXMAXMAXXAASAMAAAMMMSAMASAMASASXMASMMXAMXAXAXAMXMMMAAAMAMAXAAMMMSMMMSSXXAXAAMMMMMAAAASAMSMMMSASAAXXAAAXAXSSSSSMSSMXXAMMAMXAXXAMAASMSSMMSMMAS
XSMAXMSSMSMMAMMXSMAMMXXXSAMASXSXMXXASMXMMMMMXSSMAAXASMSSMMSSMSAMXXSMAMXMASMXSASXMMMMMMAMAXXXXAMMSMXMMMSMXMAAMXAAMAASXSMMMMMMMMMMMMAAXAXMAMMM
AMMAMSAAXMASXMXAMMASMMSMMMSXMAXAXAXAMMMSSMAXSMAMSMSAMXXMAXAAXSASMAMMAMASXSAASXSAXXXXSSSMMSSSMMMXMAMXMXAXMMMMMMMMXSXSASAMASAAXAAAAXMASMMMSSSM
AMAXMMASMXXMASAXMASAAASXAAMASMSXMMMMSXAAASMXXMXMAMMAMMSSMMSSMSAMMSMSXSMSAMMMSSSXMASXXAMXXAAAAASMXAAAMMXSAAAAAXAXXMSMASXMASMSMASXSSMMXAXXAAAS
SSMSMMMMMXSSXMASMMMSMMMMXMSAMXMAAXAAAMMSMMMXXSMMXMSAMXAASAMXMMSMXXAAAXAMAMAMMASXMMXMXMMMMMSMSMSASMSXSAXMMSSSSSMSAXXMAMAMXMXXAMXXAAXAXMMMMSMM
XAASASAAXSAMXMASAAXAXMASAXMXSASXMMMSSSXMASMSMAASAAXMASMAMSMXXAAXAMXMMMSMASASMAMMMAXSMXAXAAMMMXMAMAXAXMMXXMAXAAASMMSMXSMMASMMSMSMSMMMMSASAMXS
MMMSAMMSSMMMXMASMMXMMSAMXMASMAXXAXXAAMXSMAAAMXMMAXXXMMXSSMSMMSSMMAAXMAASASAMMAXAMSSMASASMMSASMMAMXMMMSAMSMSMSMMMMSMXAMAMASMAAXAMMXAAAAAMXSAS
SMXMAMAMXXXMAMASAMXSAMMSSMMMMAMMSMMXMAMMSMSXSMSSMMSSSMAXAAAXAAAMSSXSASMMMMMSSSSSSMAMXMAAXAXXXAXXXAASAMASXAXAXAAAMASMXSAMMSMSMSMAXASMSSMSXMAS
SAXSAMXSASMSASASAMXMASAAXAAXMAMAAXMAMSMAXXXAMXAASXXAMMSSMSMSSMSMMAAAMXXAMSMMAAXMAMAMXMXMMMSSSSMSSSXMASXMMSMSMSXMSAMMXSXSXXAAAMXMSMXAMMMXAMAM
MXMMMAAMASASASMSAMSMSSMMSSMSMAMSSMMMXMMSMMMMAMSSMXMXMAXXAXXAASAAMMMMXMMXXAAMMMMMAMXSSMAXAXMAAAXAAXXSMMMMAXAXAAXXMXSMMMMMMMSMSMAMMXMSMSXSXMAS
MAMXSMMMAMMMAMASXMAXAXMXMAMAMAXMAMXAMMAMAXASAAMAMMMSMMSMXMMXMMSXMXXMXMASXSMMXSAMXXSAXSASXSSMMMMMSMMXASAMXMMMMMSXAMXMAAAMAMXMMMXSMAXXAMXMAMAX
SMSAXAASMSSMMMAMASMMMSSSSSMSSMSMASXSXMAMMSMSAXSAMAAAAMXXSXAMSAMXMASXSMMSAMAMAMAXASAMXMMXAXAAMXMXMAMSXMAXXAXASMMMSMAMSXMSSSMMAMXMMMSMAMASXMSS
XAMMSSMSAAMXXMSSMXXXXAAMAXAAAXAMMMMXAMASAMXXMAXAMMXXSMASXMXSAASAMAMMAAMMXMSMMSSMMSSXMSSSMSSMMMSMSAMMXSAMSMMMXAAAASMXMXMMXAMMMMAMAMXMAMMSAAXA
MMMMAMMMMMSSSXAAXXMMMMSMAMMMMXXMAAAXXMAMMSSMMSSSMSXMMMMMAAXXXMMAMASXSXMAXXXAXAMAXXASAMXAXAAAMAAXSMSAAMAMAASMSSMSXMXAMASXSXMASMMSXSASASXSMMMM
XXAMSSMXAXAASMSSMMMAAAAMMMXXXMSXSMXSAMXSMAXAXMAXAAMSASXSSMSMSSSXMXSXMAMMSMSMMXSXMAMMXXXMMSSMMMXXXAMMMSXSMSMAAMMXXMSXSAXAMASASAXAAXASAXMXSAAX
SSMSAAMSSMMMMMAAXAXSXXSSSMSSMMSAAAASAMASMSMMMMAMMMXSASAAMAAASAMXMASMSAMSAAAASMMMSAXSSSSSMXMAASXSMMMSXMXMMMMMMXXAMMMAMMMSMAMASMMMSMXMXMMAMXMS
AAXXMMMAMXAMXMXMMSMXAAMAMAMXAAMSMMMXAMASMAASAMXSASAMMMMMMXASMXSASMXAXASMMMMXMAAAXAXXAAAMMAMXMAAXAXASAMMMASXSMMMMSAMXMXAMMXSXSXMAXAMXXXMASAXM
SSMSXXMAXSAMXMXXAXAMMMSAMXMMMMXMXXASXMASMSMXASASASMMAMAXMMMMMMSASXSSMXSMAAMASMMSSSMMMMMMSSSSSMMSSMASAMAMAMXAAAAXMMSMMMMSAMXMMMMAXXMXMMSAMASX
MAAXMXMMMMSMXAAMXMMXMASAMASXASAMXXMAXSXSAXMSMMXSAMXSASMSMSAAAAMAMAXAAXMMSSMASAAAAAMSMXSAAXXAXXXXMMMMAMSMASXSSMMSXAAAXAXMAXSAASMSSSMASXMXMSAX
SMXMAAXSAXAXXMXXXAXSMMMAXAMMAMXSXSXMXSAMAAASAMAMAMASMSAAASMXSSMSMSMMXSAAAAMSMMSMSSMXSAMMMSMMMSAMXAMMSMXMASAMXXMAMSSSSSMSAMXSXSAAAASXMAXAXAAX
SAASXSXSXSMSMMASMMMASASMMSMSSSMMMSAMXMAMSAMXAMXSAMXSXXAMMMXMAMXAAASXASMMSSMXAXXAAMXMMMXAAAAAAXMASASAAXAMXSAMAMMMMAMXXXXMASAMMMMMSMMMSSMMXMSM
MSMSAXXMMXXAXAAMAAAAMMSMAXAAAAXMASXMASAMMSXSXMAMXSXMXXXXSAMMASXMSMSMMSAAXAASXMMMMSAMASMMXSMMMMAMSAMXSSXSASAMXMAMMAMMMMXXAMAXAXAAAAAXAMXSAAXM
MAXMMMXSASXMSMSMSAMXSASMXMMMSMMMMSASXSXSAXXMASXMAMAMMMMMMASMASAXAAXXMMMMSAMXMXAMASXXAXAXAXMAMXSAMMXSAMAAAXXMAMASMMMAASAMSSMMSMMMSSMSSMASMSMS
MSMAMAAMXMAAAAAMXSXXMASMMMAMXMASMSAMAMAMMSMSMSAMXXAMAAAAMXMMASMMMSMSSXMXSXSAMMSSXMMASXMMXMASMMXAMAMMAMMMSSSSSMMMAASMSMMMAAAAXASAMXAAXMAXXXAX
MAMAMMSXMXMMMMMSAMXMMXMAXXAMXAMXMMXMAMAMXAAAASAMASXSSSSSSXXMASAXXXXAAXSASMSASAAMMXAXXAXXAMAMMAMAMAMMAMXXAAAXAASMSMMXXAAMMSMAXAMXXMMMMMXMAMSM
SASASXAMSSSMXAAMAXXAMXSAMMXSASXSXAXMASXSMMMMMMAMMSAAAMAAMAXMXMAMXXMMMMMASAMAMMSMASMMSSMSMSAXMASXSXSMSMMAMMMMMMMAMSMMSSMSXMASMMMSSSMSAASMSMAS
SASASMASAAAMSMSMSSSSMAMASXMAXMAXMMXSASAMASAXAXXMXSMMMMMMMMXSSMSSXSAXXSMAMMMSMMMAXAAXAAAAAMMSMMSAXAAXMAMXMMSSSXMXMAXAAXAXASAXAMAAMAASMSMAAAAS
MAMXMAMMMSMMMAXMAAAXMAXAMXXMSMSMSAAMAMAMAMASXSAMAMSXXSMMXSAMAAXAASMMAXMMSMMMASXSSSSMSSSMSMAAXSMXMMMASAMXMMAAAXSXSSMSSMMSAMASAMMSSMXMXAMAMMXS
MXMMMSXXAAAXMAMMMMMMSMSMSMMXSAAAMMSMSSMMSSXAMSAMSSSXMMASAMXSMMMMMMMMXXAXMAMSAMXMAAMMMAAXXMMSXSASXSXAXAMAXMMXMMXAAAAXXAMMXMASAMSAMXAMXMSMXSAM
SAMXAXMMSSSSMSSSMASXAMAAXAMAMXMSMXXXMAXAMXMMXMAMMXMXMSAMMSMMMXAXXMASMXMSSSMMAMXMMMMMMSMMXSMMAMAMASMXSASASMSSXSXSMMXMASXAXMXSXMMMSSXSAAAAAMAS
SASMMMAAXAAAAAAASASXMSAXMSMMSMMMXMSXSAMMSAAXMMSMMASAXMAMAAAAMSASMSASAMXAAAMXAMXXAXXAAMASASAMAMXMAMAASAMMSAAXAXAXAXSSSMMMSMAMAMAXAAASMSMXXMAM
SAMASMSMMMSMMMSMMXSAMAMAAXXAMAAXAMAAMAMMSASAXAMASASASMSMSXSMXAMXMMXSXAMMSMMMSMSMSSSMSMMMMMASXMAMXMXMMXMAXMMMMMXMXAMMAAXXAMAXAMXMMAMXMXMASMMS
MAMSMMAAAXMAMXAMXAMAMASXSSMMSSMSSMMSMSAAMXMMMXMAMASAXAXAXAMMSSMAXSAMXMAMXXSXMASAMAAXMASASXXMMSAMAMAXASMSMXXASMMAXMSSSMMSXSMSSSXXSASAMXMAMAMX
SSMMASMMMMASXMAMMAMAMXMMAAAAAAAAMMXXAMMXSAMAXMASMMMXSMMAMXMAXASXSMASXMSMMMAAMAMXMSMMSASASMAMXSASMSASMSAAMXSXXMASXMAXAMXAXMXAAAAMMAXMXAMAMSMM
XMAMAMXAAXMAASMMMSSMSSSMSMMMMSMMXXXMAMXASASMSMAXAXAASXSXSMMMMXMMXMAMMAAAASMMMXMXMAMXXXMAMMAMAMXMXAMSAMMMSASAASMMAMMSSMMMSSMMSMXMMAMMSMSMXXAS
ASXMSSSMMXMSMMMAAAAMAAXAAMASXXAXXMXSSMMMSAMXXMMSMMMXSASAMAAXMMXXMASAMSMSMSAMSASXSASXXXAASMMSXSXXXSSMMMXXMAXAXMAMMMXAAAAAAAAAXAXXMAMXAXXMASXM
XSXAXAMXSXMMSAXMMSSMMSMSMSASASXMASAXAXMMMMMMAMXAMXMAMXMAMMMXSAXAASXSMMXMAMXMSAAASAMMMSSXSAMXXMMXAXMAXAXSMSMASMXMSSMSSMMSSSMMSXMXMASXMMSMASAM
XMMMMAMAMAMASMMSMMAXAXAMXMAXMAMXXMMSMMMAMXAAAXMSSSMXMASAMXAXXSXMXAAAXSAMXMSASAMXMAAMMAMMSAMXAAMMMMSMMASXAMXAMMMMAAXMAMAAAAAASAMXMASAAAMMASAM
MMAMSAMAXAMXSMAMAMAMMSXMXSMSXMSMAAAAXASASMMSMSAAAXSAMXMMXMASMMMSMMMMXMXXAXMAMMXXMSSMAASASMMSMSXAAMASASMMSMMMSAAMSSMMSMMMSMMASMMMMXSAMMSMAMXM
XSAMSXSSSXMXXMAMAMXSXSAXAXAMXMAMSMSSMMAMXMXAAXMMMMSMSAAXAMXXAAAAAXXXASMSMSMSMSMSMAAMSMMMXAMXAMMSXSAMSAXAAMAMMMMMMAAAXASXXXMAXMASXMMMSXXMSSSM
MSXMMAMMAMSMSMMSSMXMASAMMMXXASAMMAAXXAXMAMSMSMXXSASMSAMMASAMSMSSSMXMAXXAXXXAAXAAMXMXXXXXXMMMXMAXXMAMXMMSSSSSSMSASXMMXMMAMXMXMMAMMAAAMXAXAAXA
AXMAMAMXAAAXMAMAXSXMAMXXXAMSXSXSMMMSMMASAMAAXAXXMASAMASXMMMMMAXAMMMSSMXSMSXMSMSMSMXMXMMSMSASAMXMMMMMXXAAXXXAAAMXMMSSSXMXMAXASMMSSSMSMSAMMSMM
AAAAXAMMXSXSSSMASXSMASAAMAXMASAMXAAMMAAXMSMSMMSASMMAMAMAXAXAMMMMXSAAAMAMMSAXMAMXAAASMMMAASAMXMXMAMMMSMMSSSMMMMSMMXXMAASXMXSXMASMMXAXMXAXMMMM
SMSSSMMSAMAMAXMSMAXMMMMXSMSXMXSXSMSMSMSSMXAAAASASMSXMASMSXSXSXXXAMMSMMMSASMMMAMSMSASAAMMXMXMASAMSXAAAAMXAXAXMXAAMSMMSMMAXMAXSMMAAXMMMSMMSAMX
XMMAAAAMAMSMSMXAMXMMSMMAAAXAMSMXSAXAAXMAMSXMSMMXMAAXXAXXMXSAMMMMMSAMXSXMMMMASAXXXMASMMXSAMMSASASAXMXSSMXMSMMXSMSMAAXAAXMMSAXXSSSMMSAXAMMXASA
XAMSMMMSSMXAAASMMMAXAAMSSMXSMAMAMAMXMXMAMXMXXXAXMAMAMXSAAAMAMAXAAMASAMAMAMSASMSMXMMMXXMMASAMXSXMMXSAMXXAXAASAMXAXXMSASMSAMXSAAMAAAMXMMXXMASX
SMMMAMAAMAMXXXMXXASXMSMAAMAMSMSSMAMSMSMASXAXSMSMSAXMAXSAMXSSMSSSSSXMMMAMMMMXSAAXAXMAMMSSXMMSAMAMXAMASAMMSSMMASXXMMAMAMAXMMXMAMSXMMSSMSAMSAMX
SXMSAMMSXXMSMMMSXMXAAMMXXMAMAXMAAAXAAXSAMMSMMAAASXSASXXAAAMAAAXXAXAXXXAMXASAMXMSXSMMSAAAXXMMASASMMXXMASAAAASAMMAMSASAMMMSSMSSXMXMXXXAAAMMASM
MAASXSSXXMMAXAAAAXXMSXAMSMMSAXSMMMXMXMMMXAAASXMXMMMMMXSAMXSMMMSMMMSMSSSSSXMMSAMXXXMAMMSMMSMSMSASXSXMMAMMSMMMAMXAXSAMXMSAMXAXMASXMMMSAMXMSSMM
SSMXMMAMXSSMSMSSMMXXAMAMMAXAMXSAAXASMSASXSSXMMSXXAAAAXXXSASMAASAAAAMXAAXMAMASMMMSSMSSMAMXXAAAMXMASMXMASXAXMMAMSMXMSMMXMSSMMMXXMAASASXXMMSAMX
AXMASMAXXAAMAAAAAXXMMMXMSSMSMASMMSAMAMXXAAMXMASXSSSMXSXMMASAMAXXMASMMMMMSAMXSMSMAMAAAAASAMXMMMXMMMAASXSMSSSMMMASAAAMMSMAMAMSXSMSMMASMMAXXAMX
MAMXXMASMMSMSSSXMMMMSSSXAMAXMAMXMAMMAMMSMMMASMXAMXMXAMXMMMXMASXXXMAXAAAXSMSXSASMSMSMSSMSASXSMMMSMMSMSMSAMAMXXSASMSMSMAAASAMXAXAAAMAMASMMSAMX
XSSXSAMXAXMAXXMASXSAAAMMMSSMMMSMSAMXXMAAAASXSXMMMAAMMSAXAMAAAXMASXAXSMSMSXSXMAMXXAXAMMXXAMASAMASAAXAXAMAMAMXXMXMAMAAXSSMSASMMMSMSMMSXMAXSMMX
XAAAMASMSMMXMMMXXAMMXXMAXMAMXMAAMASXMMMSXMMAMXAAMAXSXSXXXMXMMMMMMMMMMMMMMASXMAMMMMMMMSAMXMAMAMXSMMSMMXSMMAMSMMAMMMSMXMAMXXMAMAMAXMASXMXMSAMX
MMAMMAMAAXMAMMMSSSSXSAMXXAMMAMMSMAMAXXXXXSMSMAXSXSASMMASMMSMSASASMXAMAAAMAMXSAXAAXSSMXSMAMMSXMXXAAAXMXSXSAXAAMSMMAAXAAAMMMSXMASXMASXMSXXXAMX
AMAXMAXXMASAXAMXAAAASAMSSSXSSSMMMSSXMXXXAMAMXMSAAXASMSMMAAAASASASAMSSSMSMXMXSXXSMMMAMAMMAXMAMXASMXXSXAMAXXXSMMAAMSSSXSMSXAXAMASASXXAXXMMSSMM
SASMSMSMXAMMMSXMAMMMMAMAAAAAAAAMAMAMXMMMXMXSAMMMSMASAAXXXMMMMMMMMAMMAXAXAASXMXXAASXSMAXMASMMMMMMMSMMMXSMSSMMXSSXMXAXMXAXMMSXSAMAMASMMMMAAXSA
ASMAMXAXSXXSAXXSAMAXSXMMSMMMSSMMXSAMAAAASMMMMSMAXMAMXMSASMXXXAAAXXMAMMMMMMSAASMMMMAXSXSMMMMAAAXAAAAASAMXAXXAXMASMMMMMMXMAMAXAMMAMXMMAAMSSMAS
SXMAMSSMSAAMASMMASXMMAMXMXSMXMMAMSASMSMXSAAMXAMXSMMSMMAXMASMSSSSSSXAXAXAAMMMMMXSAMXMXMSAAASMSMSMSXSAMAXMAXSMMXAAXAMAASXMSAXAMSSSSXASXMXAXAMX
AXMSXXAAMMMMXSASAMXXSAMASXSAAXMAXXMMXAMMMXMMXMSMMAMMMXSAMXSXMXAMAMSSSXSSSXMSAXMAMXMMMASXMMSXMASAMXXMMMSXSAXMASMSSXXMSSMAMMMMXAAAMXXMAXMXSXXM
MASXMSMMMXXXAMMMXMMMMASAMXMMSMSMSXSSSSMAMMSSSXSMSAMAAXMMSMMAMMXMAMAXMAXXXAASMSXMASAAAXMSSMSAMXSASMSMSAAAAMMMAXSAXXMXMMMAAAAMMMSMAMXMAMSASAMX
XMXAXAMASXMMMSSMAMXAXXMMSSMAMASASXAAAXMAMXAAMASASMSMSXSASASAMAMSSSXMSMSAMMMMASMXXASXMSAMXAMMMAXAMAAAMMSMMXXMSXMXMASAAXSSSMXXAAAXAMMXSXMAXXAA
MXSMSMSASAAXAAAMAXMSMMAAAAMAXAMAMMMMMMSASMMMMAMXMASXMAMAMAMMMMMMASXAXAMAMXMMXMAMXMMSMMXMMMMSMSSSMSMMMXMAXXAMXAMXMAXMSMAAMMMSSSSSSXXAMAMAMSSM
AMAMAMMMXMMMMSSSMSAMASMMSXMXSSMMMMXSXMXAMXASMMSMMMMASXMSMSMXSMAMAMMXMMMMMAMSAMAMXMASXAXXXXAXXAAAMXMSXXSXMSXAXAMMMMMXAXSMXAMXXAXAAXMASAMAAAAM
SSMSASMMXMAMXAXAMMMSMMAXMMSAMXAXMAASXMMSMMMSAAMAAMSXMSAAAAASAMXMXXMAMAAAMXXSAXMSXMMSMMSMMMMSMMSMMAMXMAMMXMMXSAMAAMASAMXSSMSXMXMXMMSASXSMMSSM
XAASASAAASXSMMXXMAMXASAMMAMAMSXMMMXMAMAMASASMMSSMMAAXASMMAMMMXAMAMXMMSSSMXASAMSXXSAMXMAXAAMSMXAASXSASXSMAXMXSASMMXAMASAAMXMXASXMXAMXXMXMAAAX
SMMMAMMMMSMAAAASMSSSXMAMMAMAMXMMSMSSSMASXMAXXXAMXAXXMMXMXMSMXXMMASAAXMAXAMXMXMAAAMASXSASMXXXSSSXMAXASAAXMXMAXXMASMSMAMXMSASMSAXAXSMXXSAMMXSM
SAXMXMMXMXMMMMXSAAAXMASXSSSMSAMMSAAAXXAMAMXMSMMSSXMMSMASAAAMAMXSASMSMMAMXMAMMSMSMSAMAMMAMMASAMXMASMAMMMMSAMSSXMAMAXMXMSXSAXSMXMSMAMAXMAMSAXX
MMSMMMSAMMSMXMSMMMMMMAXXAMAMSMSAMMMMMMSAMXAAAASAMASAAMASMXMXMAMMASAAAMMMXXMXAXAAAMMMXMMAAXXMASMXAXMXSAMASXSAAXSSMSMMMMMMMMMMMMAAMAMXSSMMMASA
MAAXAMSASAAMAMXMAXXAMXSAXSAMXMMMSSXXXAXAXSMSSSMASAMSSMXMXAXXSXXMAMXXSAAAXSSSSMSMSMAXAXSXMXXXMAMMSSXAXAMASXMAMMXMAAXAAAAMASAAAMSMSMSSMASXMMMM
MSSSXXXXMXMMMXASMSSSSXMMMXXSXXSXAMMMMMMMMXAAMAMAMXMAXXAASXSAAASMMSXMMMMSSMAAXMXMMXMSMMMAXSSMSSSMAXMMSMMMXMASXASMSMSSSSXMAXXSMXAAAMXAMAMXAAMX
MMAAXSSSMSXMXSASAAAMAAMXSXMMMMMMAXAAAASMMMMMXSMXMXMSSSMXMAXMSMMAMAMASAMXAMMMSSXMAXXXMAMXMAAAAAMMMMSAMAAXXAMXMSMAAXXMAXAMMSAMXSMSMMMXMASXSMMS
XMMMMAAAASMMAAMMMMMMSSMAMAAAAAXSAMSMSMMAASMSXAXXXAMMAMXAMMMXMXSXMAMXSAXXAMXMMMMMSSMXSMXAXMMMMMMSXAMASXSSSMXXMAMXMSSXMMXMAAAMXMXXAASXMSXMAAXA
MXSAMXSMMMAMMSXSXXXXAXMAMASXMXMMMMMAMASMMMAAXMMASASMAMSMSAAAMXMXSSSMSXXMSMXMAMXAMAMXMASMXXAMXXAMMASXMAXAASAMXMSAMAMMSMMMMSMMAMMMSMSAXMASXMMA
AMXXMAAAXSMMXAMAXMAMMMSSXMXMASXSXAMAMAMAAMXMXSAMAMXMAMXXMXXASAMMXAAASXMSAAMSSMMXSAMSMAAMXSSSSMSSMMSAMMMXMMMSAXSAMMSAAASXMAASAMMAMXSAMSXMAMMX
SSSSMMMSMMSMMMAMSAXXSMAXSAMXAAASMMXAMSSSMMMSAMXXASXMXSXMSSSXSXSSMSMMMAXSMSMXMASAMAMXXSMSAAAAXMAAXASAMSMSXXAMMMSAMAXXSXMAMXXSASMMXAMXMXMSXMXS
AAAMASMAXMAXAXSXSXMASMAMMMMSAMXSASMXXAAAXXXMASASASAMASAMAAXAMMMAAAAMXMMXMXMASAMASASXAMAMMSMMMMMSMMSAMAASAMMMSASXMXSMMASMMMMMAMAMSAMMMAXXAMMS
MMMSAMSAMSMSSXXXMAMMXMASXAAAXXXSAMASMMMMMMXSXMMSASMMASAMMMMXMASMMMMMSXMXMAXMMSAAMASMMMXMXMXMASAAAMMMMSSMAMAMMASXSXSASAAMSASMMMXMAMSASXMXAMAM
XXXMXMMMXAMAXMXSMXMMAMAMMMSMMMAMSMAMAXMSMSASAAAMAMAMASMMSAMXMXMAXXMASAMXSMSMMMMMMXMXXMAMXMAMAXSMMMAAAXAMXMXSMAMASAMXMMMASASXMSSSMASASAMXAMAS
XSAMXSAMAAMAMMASAXASASAMSAMAAXXXAMXSSMSAAMASXMMSASXMAXMAMASMMSSMMMMAXAMMMMAAAXAXXMASMXAMAMAMSMMMSXSSMSAMSMXMMAMXMAMXXXXXMAMXXAAAXMMMMAMSXSAS
MMAAAXAMSMMSSMAXMSXSXXAAMAMSAMXMMXXAMXMMSMXMMXXMXXAMMMMXSAMAAMAMSSMMXAMAAXSSMMSMMMXXAXSSMSASXAMAMXAMXSAMMAAMMXXXAMSMMMSMSMMMMMSMMXSAMAMAXMAS
ASXMSMXMMMAMAMXMXMAMAMSMMMMMSMXSXMXMASMXMASXMASMSSMMSAMXMASMMMAMMMASMMSSSMAXAAMMSASMSMAAASXSMMMASAXXAXAMXSMSMMXMAMAAAAAAAMAAAMXXXAXXXSMSMSAS
MMMAXMMSMMASXMMAAMXMAXAAXSAAMXAAAXMMMMMXXAMASAXXAAXASMXAMAMASMMSXMXMAAAAXMAMMMMAXAMAAMMMMMMSAMMMSXMMSSSMXXMXASMMMSSSMSMSMSSSSSSMMAMSMXAXAMAS
MAMAMMASASXSAAMSSMXSASMSXXMSSMSSXMAAAMXMMMMXMSSMSMMXXMMMMAXXMAAMAMXSMMMSMMXSXAMSMSMSMMXXAXAMAMSXMAMXXAMMSAMSXMASAAXMAMAAAXAAAAAXASAAAMAMMMMM
SAMXSMASXMAMMSMAAMXMXXMAMMAAXAAMAMMSMMAXAMMXAXXAAXXMXSAMSSMASXMMAMASAMXMAMAMMXMXAXAXASMMSSMMAMXASAMMMMSASAMAXXAMMSMMSMMMSMMMMSMSAXSMMMSMMAAX
SASAAMMMAMXMAMMSSMAXMXMAXMAMMMMSSMAXMSSSXSASXXMXMSSMAMMMAASAMXASXSXSXMASAMASMMSMSMMMMMXAMAMXSMMMSASXAMMASMMMSSXXSXMAAAMAMAXXAAAMMXAXSXMASXSS
SAMXMAXSXMXMAXAXAMSSMAMSXSASXMAXMMMSAAMAAMAXAASXXAAMXMXMSMMXSSXMASAMMSAMAXAXAAAAAXMAMXMXMASAMAAXXAMMXSMAMAAXMAXMSAMSSSMASMMSAMXMSSMMXAMMMAXM
MXMMXSXMASXXMMXSAMASMAMXASAXAMSXSAMXMMSMMMMMSAMAMMSAMXSAMAAXXXMXAXASXSMSSMMSMSMSMSXSXMAXSAMASXMSMSXSMSMSMSMSAMXXSAMXMAMASAMXXMASXAXSMSMAMMMS
SMSXAMMXAMXMSSMSAMAXSASMMMSMSMAASMMXAXXAXAXAMAMMXMAMMASAXMASMMSMMMXMAMXAXSXMAAAMXMXXAMSAMXSMMAAXAMAMXXAMXXXSAXXAMAMXSMMMXAMXXXXSMMMSAAXSAMXA
MAMMMMAMSSXXAAXSXMSXMXSAXAXMASMMMSSMMMMMMMMXXAMXMMMXSASAMXSXAAAASASMSMXMASMMSMSMAXAXAMXMSASMSMMMMMMSAMMMMXASXMMMSSMMXMAXMMMMSSMSAAAMXMMMAMAM
MAMAMMSMMAMMXSMXMMMAMMSXMAMSMSXSAMXAAAASAMMXSASXXAAXMAMXMMAMMSMSXASAASAMAMAMAAAMMMMXMMMMMAMXMAMASAAXMXMAMMMMMSXMAAAXXMAMXASXSAASMMXMMMASAMXA
SAMMSAMASAMSAXMSXSSSMASMSMASMMMMAMSXMSMSASAAXAMXSMSSMMMASXAXAXXMMMMXMXXXXMXMMSMMSMSAMAASMSMXSAMXSMSXXAXASAMMASAMSXMMSMAXSAMSSMMMASXSAMASAMMS
SMSAMXSASAMXASASAAAAMAMAAMAMAAXXMMSAMXMSAMXSMAMXXMAAXAMAXSMMMMMSAAAXXSSMSMSXMAAXAASASMMSAXAAXXMMXMMMSXSASASMAMAMXMSASMAMMAMXMXMASMAAMMASAMAA
XAAMSMMXSMSMAMAMMMMMXXMMMMASMMSXMASAMMMMXSAMXSMSAMXSSMMSMMXXSAAXSMSXMXAAAASMSSSMMXMMXMAMXMMMSSSMSAMXAASXSXMMMXMMMAMASMMXSMMXSXXMASXMXSASMMXS
MMMAMXMMSASXXMSMSXXXAMSMMSMSMASXMAMAMAAAXMASXAMAMXAAAXAXAXMASMSXMXAXSSMMMXMAXXAMXMSSXMXMASXMAXAAMAMMMXMAMXSXMASAMAMAMASMMAAAXXMMAMXXXMMMASMA
XMMAMAAAMAMMMMXAXSSMMMAAXAMXMAMMMMSSXSMSSMSSMMMAMMMMMMAXSXMAMXMASMMAXAMXSSXSMSSMSAAASXMSASAMSXMMSAMAMSMSMASASAMAMXMXSAMASMMXSASMSSSMSSMSAMXS
MAMAMXMMMAMAAAMMMXMASXMSSXMAMMMXAAAAXXXMXMAMAXSXSASASMXXMXMASASMMAXMSAMASMAMAAAAAXSMMXXMASXMMAXMMASXSXXAMASAMXSXMSXXMAMXMAAXSAMAXAAAAAMMSMXM
ASXSSXSASMSSMXSAMXMSMMAAAASMSMSSSSSMXMAMSMMMSMMASAMAXMAMMAXMSASMSSMXSAMXSMAMMMMSMAXXSXSMMSAMSXMSSMMMMXMMMAMXMASAAXAMSSXMMMMXMMMXMSMMMSMAXMMX
SXAAAXSAMAAAAMSXMMSXAMMMXMXAAAAAXAMXAMAMXASAXXMAMAMSMSAASAMXMMMAAAMASAMXSMMSXXXAMASAMXXAAMAMMSMAAASXSAMXMMSMMASMMMXMAMAMSAMXXMMSXMASXMMSMMSM
MMMMMMMMMMMMMMMAMSMMSMASASMSMMMMMMMSMSAXSAMXSMMMMMMXASXXMMSAAASMSSMASAMXMAMXMXMAAXMMMSSMMSXMAAMSSMXASXXAXAXAMAMAXASMSXSMSMSMSSXMASMMMMAMAASA
AAXAXXAXXXSASASAMAMMMMMXAAAXMASAAAMXAAMAAAMAXMASAAAMXMSXAAMMXMXXMAMASAMMSAMMMASXMASXAXAMXAAMXSMMAASMMMSAXSSMMSSMMMSXMAXAMMAAAMASMMXASMAMMMMS
SSSMSSMSMMSASMXAXXSAXXSMSMSMSASMSMSMMMMXMAXXXSASXSMXMAMMMMSSXMMMSXMMMAMASMSXSASAXASMSSXMMSXMAMASMMSAAXMSMAAAAMAMXMMAMAMAMSMMASXXAXSAMMSSMXAX
XAAXAAMAAMMMMXMXSAMXSXMAAAAMMMSAXASAMXXMXXAMXSXMAXAAMAMAAXAMMSAAXXMXSAMXSAAAMXSAMXSAAAAXXMAMASAMMASMMMAMMSMMSSSMSASXMSSXMXXMAMMSSMMXXAXAAMMX
MSMMSSMMMSAAAAXMAXMAMMMSMMMSAAMMMAMAXXSMSMSMAMASXMSXSASMSMMSASMSMSAASMMMMMMSMXSASXMMMSXMASAMAMMMMAXASXXSAAAAAAMASAAXAXAAMXSMSSMAMAXMASMMMSSS
AAXAAAAXXSMMSSSXAMSAMXAAAAXSASAMMAMSAMXAAAAMASAMAAXMAXSAAASMMSAXAMMXMAMSAMXAXMSAMMAAAAXAXSXMMSXXMASAMMAMXSSMMSMAMSMAMMSMMSAMXAMASMMASXAAAAAA
SSSSSSMMXMAMMMXMAMSMMMSSSMXXMMMXSXSMSXMAMSMSXMXSMMMXMASXXSMSMMMMXMAMXAXSXMSAMXMXMSSMSXMSAMXASMXMAMAMXMMMMMAMXXMXXAXXXAXSXXXMSAMAXXASMSSMMMSM
'''

# input = '''.M.S......
# ..A..MSMS.
# .M.S.MAA..
# ..A.ASMSM.
# .M.S.M....
# ..........
# S.S.S.S.S.
# .A.A.A.A..
# M.M.M.M.M.
# ..........'''

lines = input.strip().split('\n')
graph = [list(line) for line in lines]
possible_directions = {(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)}

#returns number of xmas per position
# def xmas_catcher(graph, x, y, index = 0, word = 'XMAS'):
#     if index == len(word):
#         return 1
#     if x < 0 or y < 0 or x >= len(graph) or y >= len(graph[0]) or graph[x][y] != word[index]:
#         return 0
#     ans = 0
    
#     if graph[x][y] == word[index]:
#         for dx, dy in possible_directions:
#             ans += xmas_catcher(graph, x + dx, y + dy, index + 1, word)
#     return ans

#turns out it's not a recursion problem lol, directionality matters. search only happens in one of eight directions
def xmas_catcher(graph, x, y, direction, word='XMAS'):
    dx, dy = direction
    for i in range(len(word)):
        nx, ny = x + i*dx, y + i*dy
        if nx < 0 or ny < 0 or nx >= len(graph) or ny >= len(graph[0]) or graph[nx][ny] != word[i]:
            return 0 
    return 1

ans = 0
for x in range(len(graph)):
    for y in range(len(graph[0])):
        if graph[x][y] == 'X':
            for direction in possible_directions:
                ans += xmas_catcher(graph, x, y, direction)
            
print(ans)


#Part 2
# two diagonal MAS
#start with A and look for M and S
dict= {'M':'S', 'S':'M'}
ans = 0
def x_mas_catcher(graph, x, y):
    if x+1 >= len(graph) or y+1 >= len(graph[0]) or x - 1 < 0 or y - 1 < 0:
        return 0 
    if (graph[x+1][y+1] in 'SM' and graph[x-1][y-1] == dict.get(graph[x+1][y+1]) and
    graph[x-1][y+1] in 'SM') and graph[x+1][y-1] == dict.get(graph[x-1][y+1]):
        return 1    
    return 0
for x in range(len(graph)):
    for y in range(len(graph[0])):
        if graph[x][y] == 'A':
            ans += x_mas_catcher(graph, x, y)

print(ans)