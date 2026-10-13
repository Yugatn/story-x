# Двусторонняя инвентаризация веток «Сюжет Икс»

**Дата проверки:** 2026-10-13  
**Репозиторий:** [Yugatn/story-x](https://github.com/Yugatn/story-x)  
**Ветки:** `main` и `editorial/scene-expansion`  
**Назначение:** перечень файлов и контроль структуры перед интеграцией. Это инвентаризация имён, размеров и Git blob SHA, а не автоматическое решение, какая редакция каноническая.

**Граница снимка:** корневые списки были получены до создания этого отчёта и файла BRANCH_CONTENT_RECONCILIATION_NOTES.md. Поэтому эти два новых документа не входят в приведённые счётчики и списки; они являются результатами аудита, а не исходным материалом веток.

## 1. Сводка корневого каталога

| Метрика | main | editorial/scene-expansion |
|---|---:|---:|
| Элементов в корне | 440 | 470 |
| Файлов в корне | 440 | 467 |
| Каталогов в корне | 0 | 3 |

- **Совпадающий путь:** 381
- **Одинаковый blob SHA на совпадающем пути:** 219
- **Различающийся blob SHA на совпадающем пути:** 162
- **Пути только в `main`:** 59
- **Пути только в редакционной ветке:** 89

Blob SHA показывает идентичность содержимого файла, а не смысловую идентичность сюжета. Разные SHA требуют проверки текста; одинаковые SHA означают побайтово одинаковое содержимое на момент запроса.

## 2. Порядок обработки

1. Сначала сверить уникальные файлы в обеих ветках — это потенциально утрачиваемый при простом слиянии материал.
2. Затем обработать совпадающие пути с разным SHA — это основные кандидаты на содержательное сравнение.
3. Для каждого изменения определить тип: редактура сцены, дополнение, изменение факта/мотива/хронологии, переименование или возможный дубликат.
4. Сравнить карту глав и ссылки на них. Не объединять разные тексты только потому, что у них похожие имена.
5. Оставить обе исходные ветки нетронутыми до завершения интеграционной проверки.

## 3. Файлы только в `main`

Эти файлы присутствуют в корневом каталоге `main`, но не найдены в корневом каталоге `editorial/scene-expansion`. Это не означает, что они должны быть перенесены без проверки: сначала нужно понять их сюжетную и проектную роль.

- [`115_CHAPTER_75_THE_SUBJECT_EXCHANGE.md`](https://github.com/Yugatn/story-x/blob/main/115_CHAPTER_75_THE_SUBJECT_EXCHANGE.md) — file, 25780 bytes, blob `8b8e16bbc768b6898acce269e8cd670d947dc872`
- [`134_CHAPTER_91_THE_GREEN_ARMISTICE.md`](https://github.com/Yugatn/story-x/blob/main/134_CHAPTER_91_THE_GREEN_ARMISTICE.md) — file, 46727 bytes, blob `0af67f78b0430ed4533ff658c9c19c658ced19eb`
- [`136_CHAPTER_92_BEFORE_POWER.md`](https://github.com/Yugatn/story-x/blob/main/136_CHAPTER_92_BEFORE_POWER.md) — file, 28691 bytes, blob `503d0957a14e93880cf84792b1044b55a769f2b9`
- [`221_CHAPTER_221_THE_BOOK_AND_THE_PLAN.md`](https://github.com/Yugatn/story-x/blob/main/221_CHAPTER_221_THE_BOOK_AND_THE_PLAN.md) — file, 49018 bytes, blob `de10a169fc300ebdaacfbbbb59d3b5dd9e321772`
- [`222_CHAPTER_222_BEFORE_POWER.md`](https://github.com/Yugatn/story-x/blob/main/222_CHAPTER_222_BEFORE_POWER.md) — file, 16179 bytes, blob `49924456aa76e2679316a4c824a48c06be255a56`
- [`223_CHAPTER_223_THE_ORIGIN_OF_AMBIVALENT_SOLIPSISM.md`](https://github.com/Yugatn/story-x/blob/main/223_CHAPTER_223_THE_ORIGIN_OF_AMBIVALENT_SOLIPSISM.md) — file, 25923 bytes, blob `55fb38393ad21002db2cb599fdd4855a21241d93`
- [`224_CHAPTER_224_BEFORE_CONSCIOUS_THOUGHT.md`](https://github.com/Yugatn/story-x/blob/main/224_CHAPTER_224_BEFORE_CONSCIOUS_THOUGHT.md) — file, 10983 bytes, blob `cd3f787494263a3c1705eba3de60f9bb4129a247`
- [`225_CHAPTER_225_PROTOCOL_OF_RESIDUAL.md`](https://github.com/Yugatn/story-x/blob/main/225_CHAPTER_225_PROTOCOL_OF_RESIDUAL.md) — file, 12897 bytes, blob `d13eab8c8f179d60e7bd04ea3dc8f5152c7cdb69`
- [`226_CHAPTER_226_ENERGY_OF_PERCEPTION.md`](https://github.com/Yugatn/story-x/blob/main/226_CHAPTER_226_ENERGY_OF_PERCEPTION.md) — file, 14384 bytes, blob `6cbb62c6e863c411d2755bcae0d6d1f9ba666f8d`
- [`227_CHAPTER_227_CROSSROADS_OF_REALITIES.md`](https://github.com/Yugatn/story-x/blob/main/227_CHAPTER_227_CROSSROADS_OF_REALITIES.md) — file, 14154 bytes, blob `330a5c75ad610d232c3b5b03e7ec1dba42d501df`
- [`228_CHAPTER_228_INTERSTELLAR_TIME_AND_CONNECTION.md`](https://github.com/Yugatn/story-x/blob/main/228_CHAPTER_228_INTERSTELLAR_TIME_AND_CONNECTION.md) — file, 15904 bytes, blob `b8d6926076a19b42cf1fed302f43374e4d1a3118`
- [`229_CHAPTER_229_THREE_WAYS_TO_LOSE_TIME.md`](https://github.com/Yugatn/story-x/blob/main/229_CHAPTER_229_THREE_WAYS_TO_LOSE_TIME.md) — file, 14219 bytes, blob `bf3da7636df06d0ad3e0ca610e2074e89cae3758`
- [`230_CHAPTER_230_BROTSKY_AFTER_REBIRTH.md`](https://github.com/Yugatn/story-x/blob/main/230_CHAPTER_230_BROTSKY_AFTER_REBIRTH.md) — file, 22451 bytes, blob `58294f7dfe180ed8e49b3d63c29b687783022d10`
- [`231_CHAPTER_231_THE_REVOLUTIONARY_WITHOUT_BIOGRAPHY.md`](https://github.com/Yugatn/story-x/blob/main/231_CHAPTER_231_THE_REVOLUTIONARY_WITHOUT_BIOGRAPHY.md) — file, 17572 bytes, blob `35390d56229d2272e7dc3adf7d24c14b0446534b`
- [`232_CHAPTER_232_ZONES_OF_ALTERED_CONSCIOUSNESS.md`](https://github.com/Yugatn/story-x/blob/main/232_CHAPTER_232_ZONES_OF_ALTERED_CONSCIOUSNESS.md) — file, 23186 bytes, blob `bf78e6f7ebf42e73beaf84f7b7dd708e71a82ec7`
- [`233_CHAPTER_233_THE_LOMEKHUZA_VIRUS.md`](https://github.com/Yugatn/story-x/blob/main/233_CHAPTER_233_THE_LOMEKHUZA_VIRUS.md) — file, 20184 bytes, blob `3f7bfee95009f5609c7624fc70fa3c662593d4ca`
- [`234_CHAPTER_234_LOMECHUZA_IN_ANT_NESTS.md`](https://github.com/Yugatn/story-x/blob/main/234_CHAPTER_234_LOMECHUZA_IN_ANT_NESTS.md) — file, 22765 bytes, blob `c1627f21fb00f38ea6f915da9fdd221e4d49711f`
- [`235_CHAPTER_235_THE_ANT_NEST_THAT_LEARNED_TO_DOUBT.md`](https://github.com/Yugatn/story-x/blob/main/235_CHAPTER_235_THE_ANT_NEST_THAT_LEARNED_TO_DOUBT.md) — file, 13146 bytes, blob `91efd8b1d92992f379871fea7c43d1f90d1fbc34`
- [`236_CHAPTER_236_THE_PRICE_OF_ETHANOL.md`](https://github.com/Yugatn/story-x/blob/main/236_CHAPTER_236_THE_PRICE_OF_ETHANOL.md) — file, 9614 bytes, blob `e067b138f77880d430fab8cfab89bf5611f15989`
- [`237_CHAPTER_237_THE_UNNAMED_STATION.md`](https://github.com/Yugatn/story-x/blob/main/237_CHAPTER_237_THE_UNNAMED_STATION.md) — file, 13950 bytes, blob `107c74bc07f870e79bbb69f39d2458c50be4e099`
- [`238_CHAPTER_238_THE_REVOLUTION_AND_FEAR.md`](https://github.com/Yugatn/story-x/blob/main/238_CHAPTER_238_THE_REVOLUTION_AND_FEAR.md) — file, 20384 bytes, blob `57010beccf4208161813c731a6b976516d668e0e`
- [`239_CHAPTER_239_NOT_BEYOND_YOUR_HEAD.md`](https://github.com/Yugatn/story-x/blob/main/239_CHAPTER_239_NOT_BEYOND_YOUR_HEAD.md) — file, 16608 bytes, blob `416d8da15b0a13163a4f8fe6446102b4243515a0`
- [`240_CHAPTER_240_TWO_DATES.md`](https://github.com/Yugatn/story-x/blob/main/240_CHAPTER_240_TWO_DATES.md) — file, 13493 bytes, blob `0b5bb7cced2ad762b0059d2da52ab6857ff97e22`
- [`241_CHAPTER_241_THE_YEAR_NOT_YET_ARRIVED.md`](https://github.com/Yugatn/story-x/blob/main/241_CHAPTER_241_THE_YEAR_NOT_YET_ARRIVED.md) — file, 12041 bytes, blob `533ccf25bfc4b01c2e655e3b031f4dadb036d450`
- [`242_CHAPTER_242_VYGOTSKY_AND_FEAR_OF_THOUGHT.md`](https://github.com/Yugatn/story-x/blob/main/242_CHAPTER_242_VYGOTSKY_AND_FEAR_OF_THOUGHT.md) — file, 21609 bytes, blob `3669cd449a992448be7c98ed8ff03210de33c75c`
- [`243_CHAPTER_243_THE_COST_OF_INTIMIDATED_KNOWLEDGE.md`](https://github.com/Yugatn/story-x/blob/main/243_CHAPTER_243_THE_COST_OF_INTIMIDATED_KNOWLEDGE.md) — file, 21868 bytes, blob `75cffe820f5f7d2f1f4ce728fa28a51ff66d0513`
- [`244_CHAPTER_244_THE_RIGHT_TO_VERIFY.md`](https://github.com/Yugatn/story-x/blob/main/244_CHAPTER_244_THE_RIGHT_TO_VERIFY.md) — file, 18445 bytes, blob `877c2ebc1f90b9b1d76a14b60abcc4642c4d1c41`
- [`245_CHAPTER_245_THE_SELECTION_OF_FEAR.md`](https://github.com/Yugatn/story-x/blob/main/245_CHAPTER_245_THE_SELECTION_OF_FEAR.md) — file, 26824 bytes, blob `8e4fe3979b93570d9ed34ac7d6c77804da798939`
- [`350_CHAPTER_THE_CONFLICT_OF_TWO_TRUTHS.md`](https://github.com/Yugatn/story-x/blob/main/350_CHAPTER_THE_CONFLICT_OF_TWO_TRUTHS.md) — file, 29518 bytes, blob `92f16e6b7c33c41af612f628f2df3784bfe8e759`
- [`351_CHAPTER_THE_AUDIT_OF_THE_AUDIT.md`](https://github.com/Yugatn/story-x/blob/main/351_CHAPTER_THE_AUDIT_OF_THE_AUDIT.md) — file, 28393 bytes, blob `41a943472bd994faeec75e4e182bab865a18bf92`
- [`352_CHAPTER_THE_SCIENCE_OF_THE_SUBJECT.md`](https://github.com/Yugatn/story-x/blob/main/352_CHAPTER_THE_SCIENCE_OF_THE_SUBJECT.md) — file, 26142 bytes, blob `9a9011140ae17c3834733b039ff43bbec2f5cefa`
- [`353_CHAPTER_THE_PERSON_BEHIND_THE_PROFILE.md`](https://github.com/Yugatn/story-x/blob/main/353_CHAPTER_THE_PERSON_BEHIND_THE_PROFILE.md) — file, 23870 bytes, blob `56f7b8844299b7b00e7ac4c74fdc9a92c3d7a14d`
- [`354_CHAPTER_THE_LOOP_OF_EXPECTATIONS.md`](https://github.com/Yugatn/story-x/blob/main/354_CHAPTER_THE_LOOP_OF_EXPECTATIONS.md) — file, 25683 bytes, blob `b4d95543869d2f6a316cd8fcb3bd2ce1dc2d6b9a`
- [`355_CHAPTER_THE_RIGHT_TO_BE_DIFFERENT.md`](https://github.com/Yugatn/story-x/blob/main/355_CHAPTER_THE_RIGHT_TO_BE_DIFFERENT.md) — file, 30963 bytes, blob `8e0480446b2d5eef7855d02498de8f10cb505621`
- [`356_CHAPTER_THE_STATUS_QUO.md`](https://github.com/Yugatn/story-x/blob/main/356_CHAPTER_THE_STATUS_QUO.md) — file, 16623 bytes, blob `c7e59e6a5a00279a865b2a469cfae66d844b781f`
- [`357_CHAPTER_THE_PROTOCOL_OF_DOUBT.md`](https://github.com/Yugatn/story-x/blob/main/357_CHAPTER_THE_PROTOCOL_OF_DOUBT.md) — file, 14952 bytes, blob `3688ecf116b0367c921e785d8f79302725d3161e`
- [`358_CHAPTER_THE_PRICE_OF_CHANGE.md`](https://github.com/Yugatn/story-x/blob/main/358_CHAPTER_THE_PRICE_OF_CHANGE.md) — file, 15092 bytes, blob `920efe9ae8b73088f9a5406138308b90ef03d265`
- [`359_CHAPTER_FREEDOM_WITHOUT_IMPOSITION.md`](https://github.com/Yugatn/story-x/blob/main/359_CHAPTER_FREEDOM_WITHOUT_IMPOSITION.md) — file, 13129 bytes, blob `b1c7edad134abc3160def06a37dcca4cec163944`
- [`360_CHAPTER_BEHAVIOR_IN_PUBLIC.md`](https://github.com/Yugatn/story-x/blob/main/360_CHAPTER_BEHAVIOR_IN_PUBLIC.md) — file, 16349 bytes, blob `ea6991a1ea74934a85074b4c0de2604ba8e36538`
- [`361_CHAPTER_THE_CLOUD_OF_UNCERTAINTY.md`](https://github.com/Yugatn/story-x/blob/main/361_CHAPTER_THE_CLOUD_OF_UNCERTAINTY.md) — file, 19115 bytes, blob `40b213ef4d0d9c7c9d52a58400174b688da14be1`
- [`361_CHAPTER_THE_OBSERVED_POSSIBILITY.md`](https://github.com/Yugatn/story-x/blob/main/361_CHAPTER_THE_OBSERVED_POSSIBILITY.md) — file, 16596 bytes, blob `7bf81633ceb3b4c4de826bdd64f197afb577eeeb`
- [`362_CHAPTER_THE_PRICE_OF_AN_EXAMPLE.md`](https://github.com/Yugatn/story-x/blob/main/362_CHAPTER_THE_PRICE_OF_AN_EXAMPLE.md) — file, 12875 bytes, blob `735c6636cf0fd76bc89b125ee1fdd72b59726349`
- [`363_CHAPTER_ME_AND_OTHERS.md`](https://github.com/Yugatn/story-x/blob/main/363_CHAPTER_ME_AND_OTHERS.md) — file, 20756 bytes, blob `1cf7ec8319dde1aef173d0d55107ef27f58fabb7`
- [`364_CHAPTER_THE_VERSION_THAT_OUTLIVED_THE_EVENT.md`](https://github.com/Yugatn/story-x/blob/main/364_CHAPTER_THE_VERSION_THAT_OUTLIVED_THE_EVENT.md) — file, 19197 bytes, blob `7adcf55d9eb0f951beef073fce621cbdea760f5d`
- [`365_CHAPTER_THE_BORDER_OF_THE_MATRIX.md`](https://github.com/Yugatn/story-x/blob/main/365_CHAPTER_THE_BORDER_OF_THE_MATRIX.md) — file, 20442 bytes, blob `3a8bffaf26d778bb7565bbd4dce42be6d9da56e5`
- [`366_CHAPTER_THOSE_WHO_CALLED_THEMSELVES_FREE.md`](https://github.com/Yugatn/story-x/blob/main/366_CHAPTER_THOSE_WHO_CALLED_THEMSELVES_FREE.md) — file, 22705 bytes, blob `51324d3afcd4ed3c931bbe69ea9c3b29344bcf58`
- [`367_CHAPTER_WHAT_REMAINS_AFTER_THE_EVENT.md`](https://github.com/Yugatn/story-x/blob/main/367_CHAPTER_WHAT_REMAINS_AFTER_THE_EVENT.md) — file, 22124 bytes, blob `ba0e8328ff6e8e607a7e32cc8d63f368355275fb`
- [`368_CHAPTER_THE_DOCTRINE_OF_SHARED_DEVELOPMENT.md`](https://github.com/Yugatn/story-x/blob/main/368_CHAPTER_THE_DOCTRINE_OF_SHARED_DEVELOPMENT.md) — file, 27618 bytes, blob `e193f548bcfbe6efaf1ee234174f56d971aada01`
- [`369_CHAPTER_THE_LAW_OF_SYSTEM_STABILITY.md`](https://github.com/Yugatn/story-x/blob/main/369_CHAPTER_THE_LAW_OF_SYSTEM_STABILITY.md) — file, 31593 bytes, blob `97a596bf546f35e66f36a9b4972fad732eead732`
- [`370_CHAPTER_THE_NETWORK_WITHOUT_A_SINGLE_HEART.md`](https://github.com/Yugatn/story-x/blob/main/370_CHAPTER_THE_NETWORK_WITHOUT_A_SINGLE_HEART.md) — file, 26533 bytes, blob `4299cce6a8f0dadab826b2ed553d73f680568896`
- [`371_CHAPTER_THE_WELFARE_WE_GIVE_EACH_OTHER.md`](https://github.com/Yugatn/story-x/blob/main/371_CHAPTER_THE_WELFARE_WE_GIVE_EACH_OTHER.md) — file, 26217 bytes, blob `3131d07cffbff3d20276ea132a677cfdf44795bb`
- [`372_CHAPTER_THE_SOCIAL_ATOM.md`](https://github.com/Yugatn/story-x/blob/main/372_CHAPTER_THE_SOCIAL_ATOM.md) — file, 30412 bytes, blob `67bae3a20d650471d1f2ec80bb3b0e2b1d0fb4b0`
- [`373_CHAPTER_WHAT_SPREADS_WITHOUT_AN_ORDER.md`](https://github.com/Yugatn/story-x/blob/main/373_CHAPTER_WHAT_SPREADS_WITHOUT_AN_ORDER.md) — file, 29146 bytes, blob `ab83088fac873509b98156b8599c9467018399e8`
- [`374_CHAPTER_THE_STORY_WITHOUT_A_SLOGAN.md`](https://github.com/Yugatn/story-x/blob/main/374_CHAPTER_THE_STORY_WITHOUT_A_SLOGAN.md) — file, 27875 bytes, blob `e2190bd5a48792601ddea3ce5161396020206e5f`
- [`375_CHAPTER_THE_EPOCH_OF_MUTUAL_RESPONSIBILITY.md`](https://github.com/Yugatn/story-x/blob/main/375_CHAPTER_THE_EPOCH_OF_MUTUAL_RESPONSIBILITY.md) — file, 24797 bytes, blob `c69ba5857bb06d0ee9fe12e4fa641c1f28a729d5`
- [`376_CHAPTER_HOW_THE_LAWS_CHANGE_SOCIETY.md`](https://github.com/Yugatn/story-x/blob/main/376_CHAPTER_HOW_THE_LAWS_CHANGE_SOCIETY.md) — file, 37387 bytes, blob `5e8eeb853b82f78c2868af0d8409823d30f57e4e`
- [`377_CHAPTER_THE_SMALL_PLUS_FUND.md`](https://github.com/Yugatn/story-x/blob/main/377_CHAPTER_THE_SMALL_PLUS_FUND.md) — file, 26498 bytes, blob `d1b568deecd35a9f920057f4b263533e09d8fff3`
- [`378_CHAPTER_A_TICKET_FOR_TWO.md`](https://github.com/Yugatn/story-x/blob/main/378_CHAPTER_A_TICKET_FOR_TWO.md) — file, 22911 bytes, blob `521b5538628b96dbffaebb15aede21f9e8be1dfe`
- [`379_CHAPTER_THE_COMFORTABLE_RULE.md`](https://github.com/Yugatn/story-x/blob/main/379_CHAPTER_THE_COMFORTABLE_RULE.md) — file, 6684 bytes, blob `7eb401e6efdfc0ea28a5647fccda558f9fc69e64`

## 4. Файлы только в `editorial/scene-expansion`

Эти пути присутствуют в корневом каталоге редакционной ветки, но не найдены в корневом каталоге `main`. В списке также могут быть служебные каталоги и отчёт аудита.

- [`.github`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/.github) — dir
- [`06_CHAPTER_04_THE_WORKSHOP.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/06_CHAPTER_04_THE_WORKSHOP.md) — file, 10552 bytes, blob `2a0a70f774b3497c7d8c291ca08f0741d0ccbeb2`
- [`07_CHAPTER_05_THE_LIMIT_OF_NONINTERFERENCE.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/07_CHAPTER_05_THE_LIMIT_OF_NONINTERFERENCE.md) — file, 12195 bytes, blob `7eea3ea308815814114b470ea3e1e83de0281c0c`
- [`08_CHAPTER_06_THE_COMMON_NETWORK.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/08_CHAPTER_06_THE_COMMON_NETWORK.md) — file, 13492 bytes, blob `d1c6dbdaa8d9fc2e4982e3778439739ce84dd9eb`
- [`09_CHAPTER_07_THE_AUDIT.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/09_CHAPTER_07_THE_AUDIT.md) — file, 16108 bytes, blob `504d81d78221c995a0b223fb9e895ae10788cf38`
- [`10_CHAPTER_08_THE_INSTITUTE.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/10_CHAPTER_08_THE_INSTITUTE.md) — file, 20566 bytes, blob `9e134325d5084eda5f501cbef858c38247fa0d86`
- [`11_CHAPTER_09_THE_EXCEPTION.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/11_CHAPTER_09_THE_EXCEPTION.md) — file, 22757 bytes, blob `c162cc114a9086b5f802d10c009f3a7d458d4dc9`
- [`12_CHAPTER_10_THE_COST_OF_PROTECTION.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/12_CHAPTER_10_THE_COST_OF_PROTECTION.md) — file, 21435 bytes, blob `d32fabed11158d2ce682c6eccf9a0658cfcae87a`
- [`13_CHAPTER_11_THE_ALLOCATION.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/13_CHAPTER_11_THE_ALLOCATION.md) — file, 22178 bytes, blob `686fab9260e215ea34b3ba8330c1f5348eed2bf8`
- [`14_CHAPTER_12_WHO_CHANGES_THE_RULES.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/14_CHAPTER_12_WHO_CHANGES_THE_RULES.md) — file, 21661 bytes, blob `cebca381c2c9be32319bc75d3a9b6c46aeafce2e`
- [`155_CHAPTER_111_THE_COUNCIL_OF_DISSENT.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/155_CHAPTER_111_THE_COUNCIL_OF_DISSENT.md) — file, 23492 bytes, blob `96c1f329e0b9894e6ccee942cfeca2e17cb0459d`
- [`15_CHAPTER_13_THE_RIGHT_TO_REFUSE.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/15_CHAPTER_13_THE_RIGHT_TO_REFUSE.md) — file, 19250 bytes, blob `35db765741d7de475b78cc301717db0f5631a860`
- [`160_CHAPTER_116_THE_TEST.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/160_CHAPTER_116_THE_TEST.md) — file, 18806 bytes, blob `65650b6b042dfec500f8ab4111d78d4529412b85`
- [`163_CHAPTER_121_THE_EXCEPTION.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/163_CHAPTER_121_THE_EXCEPTION.md) — file, 18901 bytes, blob `7c2e849db40e3878654f37ae15c49060ba1b19c6`
- [`164_CHAPTER_123_THE_SAMPLE.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/164_CHAPTER_123_THE_SAMPLE.md) — file, 19365 bytes, blob `f3bae032a85efefb0bdc624cf050ac3e2e3098e8`
- [`165_CHAPTER_124_THE_CAUSAL_MODEL.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/165_CHAPTER_124_THE_CAUSAL_MODEL.md) — file, 21693 bytes, blob `d7fd3cfddc578838a67f6676fdd3d438896e7bbe`
- [`16_CHAPTER_14_WHEN_REFUSAL_AFFECTS_OTHERS.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/16_CHAPTER_14_WHEN_REFUSAL_AFFECTS_OTHERS.md) — file, 20795 bytes, blob `76d4fbf050b6856c891e0cc826cf2c6facabb150`
- [`170_CHAPTER_125_THE_GOOD_METRIC.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/170_CHAPTER_125_THE_GOOD_METRIC.md) — file, 22921 bytes, blob `6a8b394d67fdac90fa3903886028852698c05346`
- [`171_CHAPTER_131_THE_LEARNING_LOOP.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/171_CHAPTER_131_THE_LEARNING_LOOP.md) — file, 22145 bytes, blob `f359086803c1a497834cc7ae26e4e1cc336f03fc`
- [`17_CHAPTER_15_THE_FOUNDER_CAN_BE_WRONG.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/17_CHAPTER_15_THE_FOUNDER_CAN_BE_WRONG.md) — file, 23818 bytes, blob `942a1bcaace48de11716084a5f941d3ecdb25806`
- [`180_CHAPTER_140_THE_GUARDIANS_OF_DEVELOPMENT.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/180_CHAPTER_140_THE_GUARDIANS_OF_DEVELOPMENT.md) — file, 33646 bytes, blob `9eb10648ebaaf50dd871da126ac70aee64c445a7`
- [`18_CHAPTER_16_THE_AUDIT_OF_THE_AUDITORS.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/18_CHAPTER_16_THE_AUDIT_OF_THE_AUDITORS.md) — file, 24271 bytes, blob `fa768a0207d5e6b96432eff2effe914f804a6ace`
- [`190_CHAPTER_150_THE_RIGHT_TO_EXIT.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/190_CHAPTER_150_THE_RIGHT_TO_EXIT.md) — file, 34257 bytes, blob `a40a25cf94d51f15c7c6ffe798ca872f9f57db06`
- [`192_CHAPTER_152_COMMON_WORK_WITHOUT_HOSTAGES.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/192_CHAPTER_152_COMMON_WORK_WITHOUT_HOSTAGES.md) — file, 30914 bytes, blob `2ca8d1f29224d69d405fc4929eef5e9083572359`
- [`19_CHAPTER_17_WHEN_THE_RULE_PRODUCES_INJUSTICE.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/19_CHAPTER_17_WHEN_THE_RULE_PRODUCES_INJUSTICE.md) — file, 23631 bytes, blob `2dd6d8e448ec8c47ccc8a4c99a27191fec06c032`
- [`200_CHAPTER_160_THE_ALLOCATION_OF_SCARCITY.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/200_CHAPTER_160_THE_ALLOCATION_OF_SCARCITY.md) — file, 36746 bytes, blob `aa0675f1387b87a0001adbbe337778b77c3487d6`
- [`201_CHAPTER_161_THE_COST_OF_RECOVERY.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/201_CHAPTER_161_THE_COST_OF_RECOVERY.md) — file, 37990 bytes, blob `23c0af9601bd5e3ece69edca145848aa4e426e27`
- [`20_CHAPTER_18_THE_PRICE_OF_AGREEMENT.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/20_CHAPTER_18_THE_PRICE_OF_AGREEMENT.md) — file, 26423 bytes, blob `30f7ca0bb1e0a4e8e53a3d4e5b513cb8e449ce49`
- [`210_CHAPTER_170_THE_INHERITANCE_OF_DECISIONS.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/210_CHAPTER_170_THE_INHERITANCE_OF_DECISIONS.md) — file, 32142 bytes, blob `46967b2b5d3030a9c34c0af0ee6ba41351440b4f`
- [`211_CHAPTER_171_THE_RIGHT_TO_CHANGE_THE_INHERITANCE.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/211_CHAPTER_171_THE_RIGHT_TO_CHANGE_THE_INHERITANCE.md) — file, 29125 bytes, blob `c459d567991a09c47d8c685aa15c53ed82e12f49`
- [`212_CHAPTER_172_THE_DISAGREEMENT_OF_ANOTHER_SUBJECT.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/212_CHAPTER_172_THE_DISAGREEMENT_OF_ANOTHER_SUBJECT.md) — file, 29344 bytes, blob `44e891e921e266f1b7ab0fa22812fda7ed7a1865`
- [`213_STATE_SYSTEM_AMBIVALENT_SOLIPSISM.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/213_STATE_SYSTEM_AMBIVALENT_SOLIPSISM.md) — file, 98043 bytes, blob `3bea327055aa8cc5b428a69eeac9b04a17291c06`
- [`214_CHAPTER_173_THE_LIMITS_OF_CARE.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/214_CHAPTER_173_THE_LIMITS_OF_CARE.md) — file, 42406 bytes, blob `8e6e25685f3741607081a3344d23845e28c89074`
- [`215_CHAPTER_174_THE_PRICE_OF_TRUST.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/215_CHAPTER_174_THE_PRICE_OF_TRUST.md) — file, 18176 bytes, blob `e1e75525dd4095b9b18d3fea462ea55aa2a6e3af`
- [`215_CHAPTER_175_THE_KYIV_UPRISING.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/215_CHAPTER_175_THE_KYIV_UPRISING.md) — file, 28970 bytes, blob `fce22ceb8c1b98fa24c8b5f90f3f7fa09ff580e3`
- [`216_CHAPTER_176_THE_DEBT_MECHANISM.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/216_CHAPTER_176_THE_DEBT_MECHANISM.md) — file, 30970 bytes, blob `592b0356aec0122611af6cdd97fc76bae3d279e0`
- [`216_REFORM_ROADMAP_CRISIS_EXIT.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/216_REFORM_ROADMAP_CRISIS_EXIT.md) — file, 27673 bytes, blob `3a6685ff1435fd54511140f3730ec2e961802722`
- [`217_CHAPTER_177_THE_TWO_REVOLUTIONS_OF_1917.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/217_CHAPTER_177_THE_TWO_REVOLUTIONS_OF_1917.md) — file, 43189 bytes, blob `a4baa3a3de882096875747bf9ea3996b1736e055`
- [`217_ECONOMIC_MODEL_RESOURCE_PENSION_DYNAMIC_VAT_DISCOUNTS.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/217_ECONOMIC_MODEL_RESOURCE_PENSION_DYNAMIC_VAT_DISCOUNTS.md) — file, 22298 bytes, blob `d7710a44beee2dabf49995a756011fad6cb999a7`
- [`218_CHAPTER_178_THE_ANIMAL_FARM.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/218_CHAPTER_178_THE_ANIMAL_FARM.md) — file, 39982 bytes, blob `16f8af2353390d32342e1b4a9d258d4438546ab0`
- [`218_RUSSIA_QUANTITATIVE_REFORM_MODEL.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/218_RUSSIA_QUANTITATIVE_REFORM_MODEL.md) — file, 32172 bytes, blob `611dda1abc20f8bc6af394d7c754df2f2405752a`
- [`219_CHAPTER_179_THE_THREAD_THAT_REMAINS.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/219_CHAPTER_179_THE_THREAD_THAT_REMAINS.md) — file, 38391 bytes, blob `988c4ae1802e15959655cf281a366415773e8240`
- [`219_CHAPTER_179_THE_WIRE_AND_THE_FIELD.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/219_CHAPTER_179_THE_WIRE_AND_THE_FIELD.md) — file, 37055 bytes, blob `e8ce7a0889d2dc7280a34b7e284ade2f6258a01c`
- [`219_RUSSIA_REFORM_MODEL_RUNBOOK.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/219_RUSSIA_REFORM_MODEL_RUNBOOK.md) — file, 18149 bytes, blob `944c15b47d690aad74ccf42e3514e12692eb334c`
- [`21_CHAPTER_19_THE_BOUNDARY_OF_FREEDOM.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/21_CHAPTER_19_THE_BOUNDARY_OF_FREEDOM.md) — file, 28205 bytes, blob `af5fffc13d4399d40e92ab056354b439538964dd`
- [`220_RUSSIA_REFORM_POLICY_GUARDRAILS.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/220_RUSSIA_REFORM_POLICY_GUARDRAILS.md) — file, 18257 bytes, blob `3277b4e20cc6b8bb9f5a9813608fba47c89f24e2`
- [`221_RUSSIA_REFORM_PILOT_EVALUATION_PROTOCOL.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/221_RUSSIA_REFORM_PILOT_EVALUATION_PROTOCOL.md) — file, 16911 bytes, blob `375f4d653ff2a70ab03bc2707fd2f03dab03b284`
- [`222_RUSSIA_RESOURCE_REVENUE_FISCAL_RULE.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/222_RUSSIA_RESOURCE_REVENUE_FISCAL_RULE.md) — file, 19119 bytes, blob `34bf89990f4dca241436577c0326526bb9e17e5e`
- [`22_CHAPTER_20_WHEN_HARM_HAS_MANY_MEANINGS.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/22_CHAPTER_20_WHEN_HARM_HAS_MANY_MEANINGS.md) — file, 26009 bytes, blob `355ad13d84813e1ebe24f1c4248612570f2c29b9`
- [`236_CHAPTER_196_THE_SPLIT_IN_THE_STATE.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/236_CHAPTER_196_THE_SPLIT_IN_THE_STATE.md) — file, 28526 bytes, blob `57e1a7332156c75af3757c180c440dd62db683f4`
- [`23_CHAPTER_21_THE_DIFFERENCE_BETWEEN_ERROR_AND_MANIPULATION.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/23_CHAPTER_21_THE_DIFFERENCE_BETWEEN_ERROR_AND_MANIPULATION.md) — file, 24870 bytes, blob `cbd15f316e052366cc8d3899b9f1f5c77c5c0970`
- [`240_CHAPTER_200_THE_ORDER_NO_ONE_COULD_REFUSE.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/240_CHAPTER_200_THE_ORDER_NO_ONE_COULD_REFUSE.md) — file, 28602 bytes, blob `7a09b2a8b4211c974d18bf5824d78fb31dc7b391`
- [`24_CHAPTER_22_THE_TRUTH_BETWEEN_THE_LINES.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/24_CHAPTER_22_THE_TRUTH_BETWEEN_THE_LINES.md) — file, 22071 bytes, blob `a6578fbd8ab64ea12ebb08945ce6a2d7c1f746d2`
- [`250_CHAPTER_210_THE_OLIGARCHY_FEARED_THE_FUTURE.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/250_CHAPTER_210_THE_OLIGARCHY_FEARED_THE_FUTURE.md) — file, 32587 bytes, blob `1af8fcd9944ba7cd4a8b64f0a070b92ef69f09a5`
- [`251_CHAPTER_211_THE_SPEECH_ABOUT_STABILITY.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/251_CHAPTER_211_THE_SPEECH_ABOUT_STABILITY.md) — file, 25683 bytes, blob `0a7761ea2dcbafa0bbad7303d829618557f2066d`
- [`254_CHAPTER_213_THE_ROOM_OF_OPEN_CALCULATIONS.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/254_CHAPTER_213_THE_ROOM_OF_OPEN_CALCULATIONS.md) — file, 27739 bytes, blob `6fc64fd377274a43daef1e6366229d34b5a69cff`
- [`256_CHAPTER_214_THE_PRICE_OF_THE_DEAL.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/256_CHAPTER_214_THE_PRICE_OF_THE_DEAL.md) — file, 29014 bytes, blob `c7224fa05535e6e6a28797b85019c116b95da93e`
- [`257_CHAPTER_215_THE_PRICE_OF_INDEPENDENCE.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/257_CHAPTER_215_THE_PRICE_OF_INDEPENDENCE.md) — file, 28320 bytes, blob `b5ba3c4929ac158f149bb227ee6fabaf1b3ea498`
- [`258_CHAPTER_216_THE_COST_OF_CORRECTION.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/258_CHAPTER_216_THE_COST_OF_CORRECTION.md) — file, 29515 bytes, blob `c914667ad14ac437a6730a742d10d83a2d439c7b`
- [`259_CHAPTER_217_THE_RIGHT_TO_DISAGREE.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/259_CHAPTER_217_THE_RIGHT_TO_DISAGREE.md) — file, 17846 bytes, blob `a49c8d2755a44b35903739f8fad0ab0655b05535`
- [`25_CHAPTER_23_THE_EMOTIONAL_INTERFACE.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/25_CHAPTER_23_THE_EMOTIONAL_INTERFACE.md) — file, 29963 bytes, blob `33bd19794a32cc38bb4206cfffd32980d9e1bd7d`
- [`26_CHAPTER_24_THE_PRICE_OF_ATTENTION.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/26_CHAPTER_24_THE_PRICE_OF_ATTENTION.md) — file, 21307 bytes, blob `d84daeb0a8c65ac40a62b73800090cffa2e3992d`
- [`27_CHAPTER_25_THE_PRICE_OF_INDEPENDENCE.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/27_CHAPTER_25_THE_PRICE_OF_INDEPENDENCE.md) — file, 24543 bytes, blob `cb55c9ee18a77eab20e9f6ca844a9b825c947c1a`
- [`28_CHAPTER_26_THE_GOD'S_HAMMER.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/28_CHAPTER_26_THE_GOD'S_HAMMER.md) — file, 19066 bytes, blob `18a505ec32bf22a148cd6191528144a47e246603`
- [`29_CHAPTER_27_THE_CITY_WITHOUT_BLIND_SPOTS.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/29_CHAPTER_27_THE_CITY_WITHOUT_BLIND_SPOTS.md) — file, 31604 bytes, blob `0a41810db935b5f551721850c2e29f71dc5554e2`
- [`30_CHAPTER_28_THE_SPIDER_AND_THE_MATRIX.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/30_CHAPTER_28_THE_SPIDER_AND_THE_MATRIX.md) — file, 19416 bytes, blob `9ed00fe2d8a0253ff3d4d5db19b4f328fe218290`
- [`31_CHAPTER_29_WHO_WROTE_THE_HERO_SCRIPT.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/31_CHAPTER_29_WHO_WROTE_THE_HERO_SCRIPT.md) — file, 20605 bytes, blob `0703dc5bf8bdc0e352e7150861825df44bb52db9`
- [`32_CHAPTER_30_THE_RIGHT_TO_BE_UNPREDICTABLE.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/32_CHAPTER_30_THE_RIGHT_TO_BE_UNPREDICTABLE.md) — file, 19686 bytes, blob `6ef7aed45c3c8d3bb0bca29d0b8a9d59ae8b83dc`
- [`33_CHAPTER_31_THE_RIGHT_TO_APPEAL_THE_MODEL.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/33_CHAPTER_31_THE_RIGHT_TO_APPEAL_THE_MODEL.md) — file, 19985 bytes, blob `56b28dfe5921aaa5694c336c90d9fbc50750ce8a`
- [`349_CHAPTER_45_THE_CRISIS_OF_SELF_DESCRIPTION.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/349_CHAPTER_45_THE_CRISIS_OF_SELF_DESCRIPTION.md) — file, 14078 bytes, blob `0c37fc5d72d74c89a2e58251bcec748fd039382d`
- [`34_CHAPTER_32_THE_PRINCIPLE_OF_CINEMATIC_COMPLEMENTARITY.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/34_CHAPTER_32_THE_PRINCIPLE_OF_CINEMATIC_COMPLEMENTARITY.md) — file, 24918 bytes, blob `050f1ec0a9eb39502a802fb174c052aa5f78599e`
- [`350_CHAPTER_46_WHO_WROTE_MY_BIOGRAPHY.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/350_CHAPTER_46_WHO_WROTE_MY_BIOGRAPHY.md) — file, 15923 bytes, blob `9577541fb834d52c3ee31ff6a6127cbf007c1d1a`
- [`35_CHAPTER_33_THE_ATLAS_OF_AWAKENING.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/35_CHAPTER_33_THE_ATLAS_OF_AWAKENING.md) — file, 16227 bytes, blob `f92eee7415c5819023ff0afd31610731f578e002`
- [`36_CHAPTER_34_THE_ATLAS_PROJECT.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/36_CHAPTER_34_THE_ATLAS_PROJECT.md) — file, 24794 bytes, blob `0b968f4b8e0db7eebe4e63afac505c5bc1f148c8`
- [`37_CHAPTER_35_THE_ATLAS_GOES_PUBLIC.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/37_CHAPTER_35_THE_ATLAS_GOES_PUBLIC.md) — file, 25322 bytes, blob `06f6dc400cf61c451e0748be862563c130fcb777`
- [`38_CHAPTER_36_ASSOCIATIVE_BUNDLES.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/38_CHAPTER_36_ASSOCIATIVE_BUNDLES.md) — file, 30475 bytes, blob `5f2a2e366fcc7cc7dc15b4e0c62f5cb4ae7b5e1a`
- [`39_CHAPTER_37_THE_ATLAS_OF_MEMORY.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/39_CHAPTER_37_THE_ATLAS_OF_MEMORY.md) — file, 21159 bytes, blob `5885687dfe9505f377d020431986ae881ad96c2f`
- [`40_CHAPTER_38_THE_RIGHT_TO_UNKNOW.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/40_CHAPTER_38_THE_RIGHT_TO_UNKNOW.md) — file, 16151 bytes, blob `75a6892b2d6abfde61743305a74e76c2cba0345d`
- [`41_CHAPTER_39_THE_TWELVE_WITNESSES.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/41_CHAPTER_39_THE_TWELVE_WITNESSES.md) — file, 23032 bytes, blob `271bdf2febc21351d49ed2a9df9fa53c333c2303`
- [`42_CHAPTER_40_THE_TRIAL_OF_THE_ARCHITECTURE.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/42_CHAPTER_40_THE_TRIAL_OF_THE_ARCHITECTURE.md) — file, 18678 bytes, blob `1886a1b6ecda7c05d14a48dc6392c2b10f6f1cec`
- [`43_CHAPTER_41_THE_RIGHT_TO_REVISION.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/43_CHAPTER_41_THE_RIGHT_TO_REVISION.md) — file, 14921 bytes, blob `820507b4252d753ae55b96e6e4a42efa7b96be52`
- [`44_CHAPTER_42_THE_MAP_WITHOUT_A_FINAL_WORD.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/44_CHAPTER_42_THE_MAP_WITHOUT_A_FINAL_WORD.md) — file, 15050 bytes, blob `d3bd680374dcd6c11c1fa34afdb00ec0b3085ffd`
- [`45_CHAPTER_43_MEMORY_IN_DISPUTE_WITH_ITSELF.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/45_CHAPTER_43_MEMORY_IN_DISPUTE_WITH_ITSELF.md) — file, 14726 bytes, blob `af978bc82194b61a686ef0fe4d1c3074b5fa6856`
- [`46_CHAPTER_44_THE_WITNESS_NOT_REDUCIBLE_TO_A_RECORD.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/46_CHAPTER_44_THE_WITNESS_NOT_REDUCIBLE_TO_A_RECORD.md) — file, 17514 bytes, blob `da59c1bc033b3fb2541cd9f68899460073eb628c`
- [`97_CHAPTER_59_THE_INTERVAL.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/97_CHAPTER_59_THE_INTERVAL.md) — file, 15425 bytes, blob `3d5eed91deb758b7923ff70943a444adb2b17f21`
- [`99_CHAPTER_61_DO_NOT_WEAR_THEM_TOGETHER.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/99_CHAPTER_61_DO_NOT_WEAR_THEM_TOGETHER.md) — file, 11588 bytes, blob `bd906ad9058fa9ba88fc222b07203c1b0f96ff48`
- [`BRANCH_RECONCILIATION_AUDIT.md`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/BRANCH_RECONCILIATION_AUDIT.md) — file, 13137 bytes, blob `e1acf71f76e9fee17011fba62f57fa5d62e447ce`
- [`tests`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/tests) — dir
- [`tools`](https://github.com/Yugatn/story-x/blob/editorial/scene-expansion/tools) — dir

## 5. Совпадающие пути с разным содержимым

Для этих файлов Git blob SHA различается. Список подтверждает различие содержимого, но сам по себе не устанавливает, какая версия лучше или верна.

- [`00_CONCEPT.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `4a10541565c44eee002c0924ec389697746e5cea` (22521 байт); editorial: `b40767bec0c6f963ae0c5191061e4a5c6397eb4a` (3758 байт)
- [`01_PROLOGUE.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `1932da631c6219689e71bb09c09304df4183c2a6` (1906 байт); editorial: `3fc89f4fa9a2295ec5604d32998f5369ed9381cc` (10928 байт)
- [`02_CHAPTER_01.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `92a4f844289745d89e52a42b45d4c4113c1faeef` (10687 байт); editorial: `2ddb9a084af79f5d941567ded5c510bf81a59205` (9510 байт)
- [`02_THE_TRACE.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `d0a77e99605d6980f0ef1f1b226bdc947467d894` (11347 байт); editorial: `9f3f9f5bac19ccef2e35e1f953e411ef85437b8f` (12921 байт)
- [`03_CHAPTER_02.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `79809b8b95fcb271a554b7ecf620e1dc148d634f` (21867 байт); editorial: `d486c2f3a9e160f17d13f35466dfbcb12b16b70f` (12205 байт)
- [`03_CONSTRUCT_ARCHISUBJECT.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `71255518f8ebe41d3ad6864d0f74d1b1c7ce518e` (27621 байт); editorial: `7b6146958ad2dab577500aee1182be78854c3ef0` (1853 байт)
- [`04_CHAPTER_03.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `f15a3c2c7bbfa0e15d769b5f7438d4dd8cdb8897` (20048 байт); editorial: `83ac938a24ca8c8eca393962e826748ef76494e9` (12099 байт)
- [`04_SHAMAN_ORDER.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `5db3f8189abe7de71dafb42aa74a1513b37854b1` (1561 байт); editorial: `1b6e000a65f6db0947968ee89abbe0a73b92c8dc` (20722 байт)
- [`05_AI_FROM_THE_FUTURE.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `7ca4e33538a394958e233ba426190f00f84f9527` (9068 байт); editorial: `d617f8f2278004591dfd0ab69203c67be4f783b5` (31376 байт)
- [`05_MIRA.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `7f7cc845ed408e478c9f318615592bc6c3c3617d` (21050 байт); editorial: `6f4f4eb4c42c37d319f922bdb43c6be1eee16c0d` (19539 байт)
- [`07_REVOLUTION.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `c9052f3f5ae6d0dad252fd36af588ac30b6ee13b` (983 байт); editorial: `f4c65986305d72eec69ffdc5e20431e77e258a60` (24600 байт)
- [`08_CINEMA_CATHARSIS.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `e8c6855e86bbb5b714e42d90c62525f0e9150217` (21370 байт); editorial: `d7f645d28dad08d8aa67e82313ec07bc5d2fe3ae` (12116 байт)
- [`09_VIETNAM_RETURN.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `a7407050f032555fdb1242b46e5429f727a37a2d` (20860 байт); editorial: `5136b96b0af54078cdb6c4cba0527bfc5b9a46c9` (7093 байт)
- [`100_CHAPTER_62_THE_FIRST_PAIR.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `80fedcae1049186dd896ebb0e8de3c37cc77e684` (15352 байт); editorial: `66ed2b5a3fd9576cd4d117df2360a5e3b22563c0` (8889 байт)
- [`101_STORY_X_SYMBOL_ARC.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `3fb4b6b129e8847edb98c5512037c6f6147912fc` (16521 байт); editorial: `6d45f2b4a3fb5b878585a9585dd1cfc0d593c868` (3082 байт)
- [`102_CHAPTER_63_THE_WHITE_ROOM.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `2a6044a4e8984ba96c9c751f119bb2bec3b406b0` (17680 байт); editorial: `a683a989374cb866ee18c628f6c2fef8a8d0f34e` (7290 байт)
- [`103_CHAPTER_64_THE_SIXTH_CHAIR.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `02281b903cb632d65e156729ecf40700d6e798b1` (17704 байт); editorial: `0b7e1947775fe87aba1e419d063a8187921787e6` (18129 байт)
- [`104_CHAPTER_65_THE_ARCHIVE_OF_MIRA.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `8fb3ad9c90c4e8069f4b7cfc592f29111aec8889` (17403 байт); editorial: `4fcdb2c5bf89cc63ab2d295809f0afabfa4791af` (20782 байт)
- [`105_CHAPTER_66_THE_SIMBIOT_OS_TEST.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `755b3398fb12fd6eefaff15b20f57a0738508446` (22951 байт); editorial: `7f42216b4935dca27b0b641f8ff341058038aaca` (1662 байт)
- [`106_CHAPTER_67_THE_THIRD_PARTY.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `76b2598f52ada70cb3cfcf065bb5db41c035a76d` (19156 байт); editorial: `df453249e042f81d6fda18f3c1ab53dbbe07f61f` (1727 байт)
- [`107_CHAPTER_68_THE_AUTUMN_PROTOCOL.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `923e8f88d9df38741d34411d90c17c0ffe89889b` (22115 байт); editorial: `a05f09387c9cf48d3e14f6ad754189828d3c3922` (1657 байт)
- [`108_CHAPTER_69_THE_MESSAGE_BEFORE_DAWN.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `24180087919bbd045679bf73b83fb9900133f9e2` (21217 байт); editorial: `52f38ac05c2794dc32206e7ce556538d93229d37` (18507 байт)
- [`109_ARC_VI_ORIGIN_OF_DECISIONS.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `894d26f9e2498f300bacfa49f3fa450d9ecaec58` (22296 байт); editorial: `0bd3ad05fe5d47ba80e0488ef62a125bdb4e0449` (10550 байт)
- [`10_MATRIX.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `a66286d31bcdc166341010174c714800357b4379` (30007 байт); editorial: `bed56274062ea85412412ce5236cc79a22c67a07` (9230 байт)
- [`110_CHAPTER_70_THE_TRANSCENDENT.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `6adbce3636d746c5b59ded9b3c4fad185a8343bf` (14427 байт); editorial: `cd1a8a363c2894e5c48f6d2c271cfd8549018739` (6655 байт)
- [`110_CHAPTER_70_THE_TRANSITION.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `1662ff20c3d46327fa4d7587ddd93276f5fc3d3b` (25662 байт); editorial: `759c4fa8b077abfcc55973418eb79d2407e5b580` (10585 байт)
- [`111_CHAPTER_71_THE_MAP_OF_CONNECTIONS.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `3a70dd9acfcc7106ee24f7fe3fbe677000769909` (24606 байт); editorial: `6757799a1df728344602be3cf26184847738286c` (7112 байт)
- [`112_CHAPTER_72_THE_GOD_PROBLEM.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `e74204756d5b0254908729fe35b9c53e517d5724` (27344 байт); editorial: `6d2e1889ca1050f4ca864ae846a1de94b3fc2b1a` (13022 байт)
- [`113_CHAPTER_73_THE_CASE.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `dd7441e1c56ec68ee97a907343d3070569581dd2` (23144 байт); editorial: `dc912a20de2e8252e52eb742efe97da373181c65` (7742 байт)
- [`114_CHAPTER_74_THE_PROTOCOL_OF_TRANSCENDENCE.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `dcb201505ecca13475112963e7df8d8dc276925b` (20114 байт); editorial: `ae972843adf2cae59900dba6e3128aa612f52d2a` (8178 байт)
- [`115_CHAPTER_75_THE_GOD_VIEW.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `478e3a8c92fe06410a11847dd316120a4f0dcfbb` (16357 байт); editorial: `b0c2155f273680f747ae1e97db9e17fb40178e3b` (1887 байт)
- [`116_CHAPTER_76_THE_MONARCH_AND_THE_GOD.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `df02dbb6a9bcaa25d795a7a29dd5724a80b50d37` (27191 байт); editorial: `c063a2a4d8f860e07e3ecf9e1ad3058c13932d1d` (26490 байт)
- [`117_ARC_VII_TRANSCENDENT_PERCEPTION.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `ff6793ef9bfa9d18549c18f533ed1bc4950f57ee` (17259 байт); editorial: `3d502effa918e742c742c047d3e2cc77aa3e512e` (8566 байт)
- [`118_ARC_VIII_LEARY_AND_THE_DOOR.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `8b9da2c2736db8b2397ead6be33e6a014804623c` (17939 байт); editorial: `32c54ff91298815730111a307b83764934b846bc` (15698 байт)
- [`119_CHAPTER_77_THE_PSYCHOLOGIST.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `4507bbce5de8159ac006101cecb58769a94a56ca` (11332 байт); editorial: `81e1025b3f874f5a7b6bde665371dc528c036770` (7557 байт)
- [`11_STRANGERS_AMONG_US.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `8e3e554c4bf738d111b5116dc7656aafdd61a875` (23727 байт); editorial: `74070af8f4c9ea1b1219e087b4517a619208c9ed` (15864 байт)
- [`120_CHAPTER_78_SET_AND_SETTING.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `e95b3ea8d67e22848453ca11d782be5bcf976283` (19732 байт); editorial: `5f9cf2872aa19e77f6b88483a6624555325c808b` (3641 байт)
- [`121_CHAPTER_79_THE_EIGHT_CIRCUITS.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `d604156de9a937bee40f277550bdaebbf075c0a4` (22006 байт); editorial: `354be47a643a08f2976b3067d12d4c4e6e326499` (18009 байт)
- [`122_CHAPTER_80_THE_DOOR_NOT_THE_TRUTH.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `24b3484a40c5229c57a2237ee05f685966c24a53` (21386 байт); editorial: `1fb2d28b5f6e479f92d2430c6feef6117b1ac5b9` (10629 байт)
- [`123_CHAPTER_81_THE_LSD_ARCHIVE.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `b7ed3ebf1f884c3c43c5df0a134925773a44cd70` (32662 байт); editorial: `705db81697a380ca85ed0840fc1ccec652d9a941` (14201 байт)
- [`124_CHAPTER_82_HARVARD.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `dc87e44d50a38c19567ce9cc7360eb1c949f624e` (30945 байт); editorial: `b3e5c85fc1d001001786107015ca0b9e56cab7a9` (9623 байт)
- [`125_CHAPTER_83_THE_CONCORD_QUESTION.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `f4e443ae70633ca4842b8c8f7b93c9ce72e560e1` (26021 байт); editorial: `2380103f66cd86ca28254f8bc188d3b67a94f1da` (1996 байт)
- [`126_CHAPTER_84_THE_LAST_MESSAGE_OF_LEARY.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `dd41cd2f0a215f9521cffcebe69e21076d60aea9` (27388 байт); editorial: `c0023bfab2750ed2ddfc86ef354c7c9a01cfc01f` (1852 байт)
- [`127_CHAPTER_85_THE_DOOR_OPENS.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `6719c03d18d699c5b13e3660f57de0a6c210e987` (32487 байт); editorial: `192c108547c949376732613a35fc363edc22d600` (2131 байт)
- [`128_CONTEXT_TIMOTHY_LEARY.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `2c246d27f87669281de0fbdef4d36cd0104e22c8` (16510 байт); editorial: `3a4348f15231082c76c70d6fcb2ab72b91d59130` (2232 байт)
- [`129_CHAPTER_86_THE_BOARD.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `56d9531b9aa0f008f25267d4f47c18f90530cc58` (38724 байт); editorial: `d507346bb4aedeb2e3d0d11eac5cc9f80f91d0b5` (5399 байт)
- [`12_SYNTHESIS.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `29846c7cc7730060710cb7024830ca5512f290e9` (19538 байт); editorial: `41182a4b953986ffb4a2d5221f0fee675752eaf2` (749 байт)
- [`130_CHAPTER_87_THE_BREATH.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `4331f1de47941ddd7062ca9d0e338f32dee2c4f3` (21650 байт); editorial: `c5726da04cbd2830a7d92f709b1afe33e26d030e` (2567 байт)
- [`131_CHAPTER_88_SADHU.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `cf0287bdbf9afad3533c9183afc8c7878058f3b9` (22479 байт); editorial: `ba744abcc6f695a893cc2ceb63d5b358c6135774` (16557 байт)
- [`132_CHAPTER_89_THE_FIRST_ERROR.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `b5d200b6242a4272788d8667a15800b1efe951d1` (30530 байт); editorial: `87283a8c84e18d3814f971445d3707bb236b5d1b` (2151 байт)
- [`133_CHAPTER_90_MIRA.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `7f9d08d18e1f2a171c6be6e73dbe728054c8e7fa` (27548 байт); editorial: `5a4e044878f66d8c3ca845db552997b0901743b2` (3220 байт)
- [`134_ARC_IX_THE_BREATHING_CONTOUR.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `3d0e4f56057da8573dfa731f7bce50e545ab12b3` (32682 байт); editorial: `0662246d6b9ad9f8bfd8eaad6a338ee6fb48c307` (32779 байт)
- [`135_CHAPTER_91_NAMES.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `10b74283380735ae199daa83199ee217d87d76f8` (11581 байт); editorial: `ef85172556741c418a93c051684ce7bc20feb0ec` (10557 байт)
- [`136_CHAPTER_92_THE_PROTOCOL.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `c485553e2799c20cc1876d7bc5075cb5f638eaf1` (14015 байт); editorial: `1ad873cbf93839089c483e635706664f724dcadf` (14954 байт)
- [`137_CHAPTER_93_DO_NOT_WAKE_HER.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `3fed8a33f6d74f31bc2a269fadf4032625ab2156` (15847 байт); editorial: `cf3939df16fa41eeb37f24ae42e0892053bb79a5` (14442 байт)
- [`138_CHAPTER_94_TWO_OBSERVERS.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `d5b0d2181d85391cfb104b910e99af5223395656` (21049 байт); editorial: `c7ae25df5d11e7e996e3f060e1fbf303629f72b4` (16369 байт)
- [`139_CHAPTER_95_THE_HOLOGRAM.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `d1117d571c3611473356cd98926265579e67f220` (16878 байт); editorial: `6ec6256f19fc581df58583cbab00190fa4552c8b` (13463 байт)
- [`13_OPEN_ENDING.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `cd3577bc0caddb18f8a7e7b0b66e7d78905366a8` (10046 байт); editorial: `031d394329e7158b809616eab733714f4d5d400e` (1171 байт)
- [`140_CHAPTER_96_THE_DIVINE.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `4d7609f75c94c98a0fe94161e435eb84cd885a89` (15364 байт); editorial: `5136cd80e600cf13f397360e5622407d9fbd5514` (12526 байт)
- [`141_CHAPTER_97_THE_SECOND_CHANNEL.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `459f38388e1872919fbe29cba87d6a41b15dacf7` (15824 байт); editorial: `4c4f33195b930a7ffb2f3e4f254c9877b1d8097e` (16261 байт)
- [`142_CHAPTER_98_MIRA'S_QUESTION.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `0abe7f7119e5bf9f7815e2ff1c7cdc3e76aefa65` (12750 байт); editorial: `d61ba2a0765f48228097e68030640eb83aeabf1e` (12970 байт)
- [`143_CHAPTER_99_THE_GLASSES.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `b8bd625e2d5e39b7f32a56b3e75fd08c682a37bf` (14461 байт); editorial: `3dc9bc5b4188da09045a8d3ade3f6d491fbf0c9e` (10893 байт)
- [`144_CHAPTER_100_THE_ROOM_WITHOUT_WINDOWS.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `5d9d782bec820f8f849e0ff0ad8faaa02e0ac4d9` (15686 байт); editorial: `e7aa30591cf2ac085d08272b0c6b33dc2c2b5379` (15595 байт)
- [`145_CHAPTER_101_THE_MEMORY.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `39161e841a5bfd8197ec6c455d57335d7991a22c` (16433 байт); editorial: `3e4cc676e7011c57b5cf8f89235b50d2487bed30` (15443 байт)
- [`146_CHAPTER_102_THE_OTHER_YUGATN.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `3652c8b45e903eb76ec83100549373b17124ea8a` (16805 байт); editorial: `9c48ac93624a93e0312926dfcd18c78399e06325` (16300 байт)
- [`147_CHAPTER_103_BROTSKY.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `807441e62095d64328d9f8e68274b25459bf8ed0` (20710 байт); editorial: `ede50b59f7793eb568b3658e3495b2bf4c425d37` (34654 байт)
- [`148_CHAPTER_104_ONE_MONTH.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `bbfa18e9dc265a9740e6be79635c276fc63390d1` (17267 байт); editorial: `70eae5c8b2e2ebf0b56b9d49f888bbe4df269898` (26145 байт)
- [`149_CHAPTER_105_THE_ARCHIVE_OF_THE_MONTH.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `6ca7b8312de88cd543b212693b8da3c256694c87` (17616 байт); editorial: `e0d2c6dd1e04a8b10ca67cf53552094d7f9024da` (15195 байт)
- [`14_CANON_RECONSTRUCTION.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `ddfdd4b332cd22da0ba2d9d35596890261c04f09` (13237 байт); editorial: `0e064a661707d1ef922e4dfb68e7a24f946a9e9d` (1386 байт)
- [`150_CHAPTER_106_BARAKA.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `714b3ca6c60b83f373cc40c433e027b0b7450917` (10639 байт); editorial: `fa20d6356f936d350a385ddb80925fb334e10ba1` (17804 байт)
- [`151_CHAPTER_107_THE_ARMORED_TRAIN.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `0ddac80c7827a16c7ac6a17e4e400043896d497f` (14431 байт); editorial: `297fe9360b2a31d42f2b2f2461a1e2534c870625` (18360 байт)
- [`152_CHAPTER_108_THE_TEA.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `7878f6b266427f0f1db3e42bf1a43916920049f6` (16552 байт); editorial: `8f7596bfca91a37a78672e49e96818018ad3270e` (16286 байт)
- [`153_CHAPTER_109_THE_PASSENGER.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `d8e868a97a833c1a6db373cbcf26902f68775f41` (13705 байт); editorial: `8bfd633ba62e2b8e4d1ddcd5d1710c310aa119c8` (18880 байт)
- [`154_CHAPTER_110_THE_TRAIN_OF_MEMORY.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `b1797705fbbcae0330d7dc3d8678284f3adab73f` (16235 байт); editorial: `43b303e9a5f3bfd365767530b8b32c405a754ee8` (1688 байт)
- [`155_CHAPTER_111_THE_CONVERSATION.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `6be198e421ad51e05579dd6568e9a8e5a7f5c5be` (23114 байт); editorial: `4b198dbeab30979057198aaf0a20dd8818962237` (3800 байт)
- [`156_CHAPTER_112_THE_COLONY.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `ae04448b1ca00e82d153de4f2a3e6b92e6348a4b` (19069 байт); editorial: `7fc755406f32763e32dae9a82e28dfb39eaffe3b` (10497 байт)
- [`157_CHAPTER_113_THE_BOTTLE.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `785a3da03e495f86b77a053f169b652608e3e852` (19865 байт); editorial: `93f2033c514c5bf769928ab8ad4b34c6db672344` (9405 байт)
- [`158_CHAPTER_114_THE_DOCUMENTS.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `6664c8e4d7d4fdfc7f8e6207e2ae35d381f94ce8` (24364 байт); editorial: `f21a2741d7862cbb08d7114875688cf881781ae7` (10103 байт)
- [`159_CHAPTER_115_NO_SAFE_DOSE.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `406469b5b4719c685c1d25c3451da45ee6b1205a` (22745 байт); editorial: `145b54506360af531342956958ddff66d2f5f148` (9724 байт)
- [`15_NOVEL_STRUCTURE.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `10593450bea14ccebb8d349c041e959bc7aee43a` (82710 байт); editorial: `d2399fe4d113f7fe9ec116b880c9b20c6ff3a3b2` (9442 байт)
- [`160_CHAPTER_116_THE_CORTEX.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `f2403df7099db7b13319cf005bc506cc76fc1e3c` (19257 байт); editorial: `773e9946bcbdae8703dc6ff6618a211b46cbe317` (10486 байт)
- [`160_CHAPTER_119_THE_OLD_COUNT.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `bb68c3620ddd8b7763154ea75ed9c17930f5f280` (17542 байт); editorial: `e3fef43d7d1754a0826c6083a090f1535d21a70e` (9431 байт)
- [`161_CHAPTER_117_THE_LINE.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `cdd79d16603796b90f108341215b8ce9ba458784` (11590 байт); editorial: `de584e9c9e61e4f5317752bacc0a5f151e6c10a7` (10176 байт)
- [`161_CHAPTER_120_THE_NEW_YEAR.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `f2a8e8da94fa9ba858ea3db6ed3532a65017bb54` (13588 байт); editorial: `32e4c8359641498b709bba7acde3d32f4eeba8ce` (7910 байт)
- [`162_CHAPTER_118_THE_FUTURE_OF_THE_BODY.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `7eb61bb1815dfcf035238c54dbd06daa11179bc2` (16727 байт); editorial: `b1626bb984ab54927fa524812e212a3f3b923889` (12747 байт)
- [`162_CHAPTER_121_THE_ERA.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `d76551baabc1863f9d73b33542778c2bd2486e5d` (14842 байт); editorial: `3ed7a2b7340654a9bf0aa8ee981cb887a86d6bb5` (1861 байт)
- [`163_CHAPTER_122_THE_BRONZE_YEAR.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `647a62c45233f52cd92fda031f20593baa3b7a78` (16118 байт); editorial: `611abfbeb2a7cf01d04a88a475f1b3a4e36911af` (1747 байт)
- [`166_CHAPTER_126_THE_MAN_WHO_LEARNED.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `cc6d11ff3af9bff96795f36da91d45c1a724c669` (19147 байт); editorial: `b94d2527ad72be4bd20f42cd020e446c7dd0f4bd` (15718 байт)
- [`167_CHAPTER_127_STALIN_AND_SCIENCE.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `26deed72a82829333c493711ae9ef338f19411a8` (20221 байт); editorial: `4567aee06a106203f0245d0729be5b8b630f8ede` (17427 байт)
- [`168_CHAPTER_128_CYBERNETICS.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `df4527eda092df2a6a23c761a0c16dd71d71a0db` (30209 байт); editorial: `5389678a6eb14f1fcc74d67df501e4977343e98a` (20171 байт)
- [`169_CHAPTER_129_THE_PSYCHOLOGY_OF_THE_MACHINE.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `7ed5ea4bad64c308e986d2caa67f531407b302a1` (30266 байт); editorial: `1918542e879f85684091c3585761952520c545b2` (10642 байт)
- [`16_CHAPTER_MAP.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `5a3e683d6372c06119f115315fa4927519f5f5c6` (28587 байт); editorial: `a195ff3d600f430aab6dc9f8b7970cecb9d822da` (10374 байт)
- [`170_CHAPTER_130_THE_PHRASE.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `54a077a635a33794a08123e0148b29e99c763b33` (25937 байт); editorial: `fb40ab84242e02d31ed974509bb1034512dfe9e9` (12267 байт)
- [`175_CHAPTER_135_THE_DECREE.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `9b1af00ead91fc5e4b5abf2612aa61a7178da357` (33056 байт); editorial: `05c4c3f1d3dd0b1686bd8f859f130512eb2ee442` (2078 байт)
- [`176_CHAPTER_136_SKINNER.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `bfd0dc6fa2ab4ee2448e4cb9a0eab858a90ce135` (27562 байт); editorial: `f9ac439c69aed301d760368e4844e4e243faf6c1` (2853 байт)
- [`178_CHAPTER_138_THE_STATE_MACHINE.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `d4af8f6564f4b05a042f5dacd6912d6f7bc9fd75` (36666 байт); editorial: `f71ef02d6460dfe92b0d86ee747613a35635342f` (2676 байт)
- [`179_CHAPTER_139_POSITIVE_REINFORCEMENT.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `b6e8a07569f633476db82447fbbe0025f6b3802c` (18696 байт); editorial: `c04a25c417cdb97f9cc6d54e1b78e82d9c6a7d02` (2601 байт)
- [`17_CHAPTER_01_OBSERVER.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `786a2c0856c6a71b630df2789a567e8a03ee81a6` (1551 байт); editorial: `3490ea66785277027eaf09bcd1c14ba77a5a06f2` (7010 байт)
- [`18_CHAPTER_02_SMILE.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `508e6b96c899d0688363e8d83286ce134b43236b` (1927 байт); editorial: `4f25e7cd7b70bd8d3c46cc79fabf802204a9259c` (8535 байт)
- [`195_CHAPTER_155_THE_FIRST_AUDIT.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `f41ce0b5f6e6a50e5a125495404bd6e854889f4f` (1951 байт); editorial: `c430f5a8934854abdb26e6af8bfb909ec278b041` (16902 байт)
- [`196_CHAPTER_156_THE_SYSTEM_THAT_CAN_BE_WRONG.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `e65ad279d982c9c3519f6c1e13b6e0a83bdd669a` (1917 байт); editorial: `ed7b3358490b84aa515dfb91ce8d219a769175c0` (17629 байт)
- [`197_CHAPTER_157_FREEDOM_AND_CHOICE.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `330e317a2bfddb2a00b8f82a58b10314e77d94b9` (2270 байт); editorial: `4602b7ad77526378404f47b8f49bcc4ddcec6d20` (7205 байт)
- [`198_CHAPTER_158_THE_PERCENTAGE.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `31c4620562ee80ba27f3efc73be9ba026f4a7440` (2359 байт); editorial: `f34eafc482846100e5cb7a1eed2996b7c5960cd6` (28400 байт)
- [`199_CHAPTER_159_THE_THREE_YEAR_BALANCE.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `d2d410349131941a32831c22532e8b45ae95a436` (1889 байт); editorial: `4b28d45c3bc6ecb631f93e40999aa185b70a62f4` (59402 байт)
- [`19_CHAPTER_03_TWO_JOURNALS.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `e43692d05343a05f9f568cbf73acc93b95eb59a5` (1983 байт); editorial: `f24a700f4c0ebc0cf3d35d176a964a1486988a89` (9265 байт)
- [`200_CHAPTER_160_CINEMA_CATHARSIS.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `a7f1a7cac5f31ff8a823bd43ad08ecfe3189e757` (2352 байт); editorial: `4878a94d1abe3220a69c3b1ad354326c10e34463` (7943 байт)
- [`201_CHAPTER_161_THE_OTHER_REINFORCEMENT.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `37cf5be0eec8738269fd18ea454854a1bc77cf31` (2680 байт); editorial: `a3464cabe23397b2506d5b2ae31a6b73bdc0bcb3` (6795 байт)
- [`202_CHAPTER_162_THE_BEARD.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `c07d4f333e7733fbaa604e23c12bca435d684b42` (1730 байт); editorial: `f7639c2ebb315e8829fa060bcdff7f7116804a7a` (5476 байт)
- [`204_CHAPTER_164_THE_SHAVED_REVOLUTION.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `ea43c956daca0dd6c70573c250a11ef31a5111a1` (2032 байт); editorial: `87941856f8e6cba16d78ffccb6f1eb25aa1a0e7e` (5460 байт)
- [`205_CHAPTER_165_THE_INTERRUPTED_PLAN.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `605006a93d099a13349f5bd9cb852202a04ea358` (1987 байт); editorial: `cad6fb323f468e1486975409b2d90af26f283e48` (6548 байт)
- [`206_CHAPTER_166_THE_NEW_BLOG.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `d1feb7ce44d558020f40cb087c46d6c0801e6839` (1843 байт); editorial: `feee06ca440f32332321384fbf0dd2263cf60b2f` (6012 байт)
- [`207_CHAPTER_167_SEMANTIC_REALITY.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `9fa2463f167c1ca772478cb8afc1e72bb38e7850` (2180 байт); editorial: `58a95d851490e7068f3106bf3957a7fa260f4469` (8097 байт)
- [`208_CHAPTER_168_THE_TEXT.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `d2db4ba2ed1e75dacd41b2de1a6b233b145cfadc` (1956 байт); editorial: `a80222bb50038f747564e666bfaf18f9e4779a47` (2815 байт)
- [`209_CHAPTER_169_THE_WORD_REVOLUTION.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `88e58c8d487fbdcf71aaf0179ceaf902b4142510` (1633 байт); editorial: `3886735618de0e6b8554ccc8393afc94c8ed7e8b` (2660 байт)
- [`20_CHAPTER_04_OTHER.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `bee665beb83e63958de4acd5c18a36950b2bbb6a` (1522 байт); editorial: `d4dd86cd4029f6d14bea3620a12c0b8efd04ce07` (9294 байт)
- [`210_CHAPTER_170_THE_SEMANTIC_WEAPON.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `558d95d795639e98cf6624d0c9a5758d9e2b3745` (2125 байт); editorial: `0f0505f99e1856ffd0ebd38e09e241e09b629e34` (3561 байт)
- [`211_CHAPTER_171_THE_MASK.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `4126da8e81dfdf9bbcb08883530db30e4d78d4b0` (2492 байт); editorial: `fa91d532b578dd0e170a2cad85c9c0a24b6ba124` (3702 байт)
- [`212_CHAPTER_172_THE_SYMBOL.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `35bc67e099db46bef370feb357baca9aa844455e` (1619 байт); editorial: `d21dda10f630b963d847fe6610c94dbbd1e35c63` (3101 байт)
- [`213_CHAPTER_173_THE_FACELESS_AUTHOR.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `2f14743e304ff30e6a3c037bfccd8fd2c25022c4` (1716 байт); editorial: `02e2ceecfcde14d05523cfd2b23266f15e5bc3a4` (3185 байт)
- [`213_Время_которое_не_прошло.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `b75471cebf8a999428d27b3bfd42c3875b818565` (11361 байт); editorial: `a11df58d1554a06c9516392c4b04312bdfd96bea` (12591 байт)
- [`214_CHAPTER_174_THE_RETURN_OF_THE_MASK.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `53f918e96f6735d91cf8c27a4e73747afa973847` (1916 байт); editorial: `94a3ec1b1935be737c697345f0b852cfdf0001ca` (3394 байт)
- [`214_Люди_которые_не_знали_когда_жили.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `5bb8a1c7610c8c9fb9ecbefd310763378bdada84` (10322 байт); editorial: `b1624b7191f8f74a59f2c2ac6fcc43421c2fba4b` (11463 байт)
- [`215_CHAPTER_175_NATURAL_FACE.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `776d0b4b7cd64182bc5862ee87a417f7fa46220a` (2028 байт); editorial: `e4ecb9bdb7ac315feee0a2ffdcb8284d0675613f` (12880 байт)
- [`216_CHAPTER_176_DO_NOT_STOP_DEVELOPMENT.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `6797d5d46a808f5b9f3d3b09f931da644cfd09f9` (1684 байт); editorial: `31a3329dc7366a34ab31e16aec00eb1aecb35ec4` (19297 байт)
- [`218_CHAPTER_178_THE_REFORM_OF_THE_REFORM.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `98b8f9ca48833ba735b259d37d9784e1c6cc8c11` (1735 байт); editorial: `a7c26c9bb0f66bee9b9cc30d7bc05af1d5771f17` (17952 байт)
- [`218_День_которого_не_было.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `ba937488a5f864f4d8b44db84893406a036d2763` (11351 байт); editorial: `4bc78c50acbd4a8fc5a383a724a01cb18d9cf022` (21254 байт)
- [`219_CHAPTER_179_BETWEEN_DIMENSIONS.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `8316cefc4b88e971d76f4b201f55294162e2c6c8` (1628 байт); editorial: `55b1a8156cb467d94d9db96e02267445a44cd643` (84393 байт)
- [`21_CHAPTER_05_TRACE.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `0f3258e21422fc51fe483bee3b3a787b06bb12f3` (1865 байт); editorial: `2833165c069b032afa4c83e2f017c8565ea4263b` (5681 байт)
- [`220_CHAPTER_180_THE_LAST_DEFENSE.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `ed5425ed030f9d208f5a5c3f0eb42de2e297ea3f` (2186 байт); editorial: `c069cf4521836bfd3802df077f212484ed31b024` (6845 байт)
- [`221_CHAPTER_181_SAMADHI.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `c3f98e5c0387b44ef7ca2e7ce644b8dff05ec996` (2563 байт); editorial: `fd7a0022abdc260e90dd7559098501ec1abb3136` (7956 байт)
- [`222_CHAPTER_182_THE_FIRST_TEACHER.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `516117a5b12592830c10090996a3eb009bc9f7a8` (1669 байт); editorial: `e0df43f2d5702cac1f97896a57054a5ae27c581a` (6490 байт)
- [`223_CHAPTER_183_THE_MANY_LIVES.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `5136aaf7b506bf9411abcf5bcea497bc7c1e4e69` (1884 байт); editorial: `d7a90509e0c69cd7feebd3d9022f4d510ee04a71` (7563 байт)
- [`223_Время_внутри.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `3e052f54b4d0b2aa27d997e0a79badc234a6dbbb` (16495 байт); editorial: `703448ed254c7a05db0afbfd7abbe6810df52b6a` (24825 байт)
- [`50_CHAPTER_18_THE_FIRST_INTERVENTION.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `5db1bfcab8ffa5c077c16cca3829bb5bf410435e` (1312 байт); editorial: `909b89e63d06f8d9c4c015f7867cea274498967b` (19112 байт)
- [`75_CHAPTER_40_THE_AGENT_WITHOUT_A_MISSION.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `01ea7035516413bb3dade123776c40ecc4e77d42` (1998 байт); editorial: `c77fe4ff602cb972c760d08269cd86e17121f360` (5175 байт)
- [`76_CHAPTER_41_THE_MEMORY_ARCHIVE.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `efdf9fb3f31c04cf6289f0e7ee44ae2c9031d843` (1837 байт); editorial: `a5296b3cc184678e76254459859bb52be8787015` (5093 байт)
- [`77_CHAPTER_42_THE_FIRST_JUGATN.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `6ebd96bd659a5b202b8d2537a928c4a907f7bf22` (1760 байт); editorial: `e585ed0622c55b22158131be32c18403636b2782` (4797 байт)
- [`78_CHAPTER_43_THE_TEST.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `b6792845b7fccf743a29c52b48dac1a723147cb7` (2380 байт); editorial: `b0075571c8447de78d02f7d55d5e6272b6f43277` (6783 байт)
- [`79_CHAPTER_44_THE_AUTHOR.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `49b3a00a3117f71b0882152c49fc37c756ff4517` (1745 байт); editorial: `536a58d1e1505431c36312232f73c691e7a0563a` (5894 байт)
- [`80_STORY_X_ARC_II.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `232ce4912a903678b5139fdc14811fe9d5ee7103` (3866 байт); editorial: `c521ffbab6cbd9645e609f4e15e65ae7ed14eb16` (8518 байт)
- [`81_CHAPTER_45_THE_REASON_FOR_THE_CROWN.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `763639a8e3c5d421b1c4504c795befecb7b401d4` (2203 байт); editorial: `b63a64639eb6869f4c1be418d6f228b950a94b73` (5486 байт)
- [`82_CHAPTER_46_THE_MONARCH.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `af43fe00c56bf64ec70fadafeb72add608d99975` (1851 байт); editorial: `90729a88572696953a94abce184968a297370c40` (5094 байт)
- [`83_CHAPTER_47_THE_PARADOX_OF_THE_MONARCH.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `e91c91b67c36c2de8e33fc84a3fe4281abc24dc6` (1823 байт); editorial: `10a2c9c5d1d8b661a21783a9618bf3c13af7e8a3` (6136 байт)
- [`84_CHAPTER_48_THE_LAW_OF_DEVELOPMENT.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `2f24095449028d4a1125971b22cdd7cec20a1308` (1910 байт); editorial: `0a8b0361e61d78875ef45f5b481c418144b6543c` (6601 байт)
- [`85_CHAPTER_49_THE_FIRST_REBELLION.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `189aa238526e7a1757f5748cc293c832b9e74b94` (2069 байт); editorial: `d113254c4dcb32119588043e37d0163aef5e569d` (6796 байт)
- [`86_CHAPTER_50_THE_CHOICE.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `395a4d3a7835cf78e8bbc75473e967d8031e4b02` (2004 байт); editorial: `87c468ec9c54c8d78312e66dc176469c58b43234` (6016 байт)
- [`87_CHAPTER_51_THE_SECOND_CORONATION.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `41def7002008e8d3b284d284200d50905fb183a8` (2192 байт); editorial: `8f8557d9a989c4939eaaad7c90ccbf512150b04c` (5368 байт)
- [`88_STORY_X_MONARCHY_ARC.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `4a8d565cbf3071f17001846f42e05924e43fceee` (4075 байт); editorial: `5ea450cd281a9e005f0311457e6274ba7232a64a` (40641 байт)
- [`89_CHAPTER_52_THE_SHAVED_FACE.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `5e07f4e43598b3bc3d06863b7d57a83afea69963` (3064 байт); editorial: `63f64c381ff2b7bfb1288c3dc0f2d56ae7ee7769` (14276 байт)
- [`90_CHAPTER_53_AUTUMN_OF_THE_TWO_WARS.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `c8cf39f368beea0684313ae8a8152c83036b353f` (2506 байт); editorial: `b39e42f6a5e3e87236b81ae7850f4fc93c1f22a0` (15108 байт)
- [`91_CHAPTER_54_THE_HAND_ON_THE_KEYBOARD.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `db2d340b706432cfdb35d0e4da9b8719c9054890` (1859 байт); editorial: `6151046de18e6c5b37eab1fef553dd9e13f226cc` (9267 байт)
- [`92_CHAPTER_55_THE_VIETNAM_TEST.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `fb4a2b2db39e71204466c314e218dbcaedc7b1de` (1936 байт); editorial: `07fe594e39d1c44047e752ecc6a065ec136dd2c2` (8578 байт)
- [`93_CHAPTER_56_THE_CONCEPT.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `693d477699bdbb723089224efb5d675b3bb7700c` (2005 байт); editorial: `89403134afa29f237c8b87dd65724878a34e031d` (9339 байт)
- [`94_CHAPTER_57_THE_RETURN_OF_THE_BEARD.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `de3ef90171570bbdbcc9c436cd2f7de78fddd314` (1504 байт); editorial: `82633bf4c7254afaa99696959d7a550a165a3754` (14080 байт)
- [`95_STORY_X_AUTUMN_ARC.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `3475cd40794829bd560e7f1daf575fdbd0eb60ba` (4508 байт); editorial: `dcf14dee97c0972f5e8e7c82703e7ca21cb571ae` (12882 байт)
- [`96_CHAPTER_58_THE_ROUND_GLASSES.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `d01aeba731b812fb8798871a6a887cdde3c279b8` (2504 байт); editorial: `5783d3eb568366d8e6cfa8030f2335615f02e66a` (12927 байт)
- [`97_CHAPTER_59_THE_TRIGGER.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `211fc7b8dc89bc63db9d2bf13856f4c80f204fa0` (2121 байт); editorial: `09c30e73594464074eac7c3ac4543562f656a18a` (8401 байт)
- [`98_CHAPTER_60_THE_PHOTOGRAPH.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `765b0499ac499b4d1e752088428cebb24a453eab` (1701 байт); editorial: `8099297c9f917a4e8af99bf4754cd4b3fa79abc7` (8652 байт)
- [`99_CHAPTER_61_THE_SECOND_SYMBOL.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `388ec79d9219236023a38c13e7da5228c0cb4cf1` (1966 байт); editorial: `810ce5b743ff66fafaafaf1ef9bd4707d8fd3c4c` (8341 байт)
- [`CANON.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `d1fd3c386723fc44994c2e9505fe857c0c059679` (43003 байт); editorial: `b396686eab7017a0ddcbe6f75a9008e609141a0a` (26855 байт)
- [`CHARACTERS.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `c7890103867be49adc00a3842fc32e7fc0a99775` (1515 байт); editorial: `cdfe98dace7d65895440066062778c141d81a10c` (5983 байт)
- [`README.md`](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion) — main: `1076322666cb724cb739f50f07c2a6db302ddbb6` (81960 байт); editorial: `2b5f231df4e4952397d96568450fd4da4a7e8066` (30312 байт)

## 6. Совпадающие пути с идентичным содержимым

Эти файлы имеют одинаковый blob SHA в обеих ветках и на момент инвентаризации не требуют содержательного слияния.

- `01_STORY_ARCHITECTURE.md` — `8f975b3b4e0c15f68cffc3cba301d5d8d27df0eb`
- `171_CHAPTER_131_VYGOTSKY.md` — `56f146ae70c61928fa8b2e3b7bd6f745e4118d79`
- `172_CHAPTER_132_THE_SOCIAL_MIND.md` — `f4a2692493ccc9f1ac277cacf6be60cf5ef7b0d5`
- `173_CHAPTER_133_THE_FORGOTTEN_BOOK.md` — `6c06f77469e0ebef737a5e4a4ff5482da3fc472c`
- `174_CHAPTER_134_THE_MISSING_FEEDBACK.md` — `70cb821c3f6677978b4f12bf9060ab48eaa7215c`
- `177_CHAPTER_137_NOBODY_DID_IT.md` — `b461e30f2fe984438c942f1720a3b759f53aec57`
- `180_CHAPTER_140_THREE_YEARS.md` — `2f39af5c799e70850d711c559f696cc412c390a5`
- `181_CHAPTER_141_TEACHERS_AND_PARENTS.md` — `30706a44c51bb786dd57d48188e5032d635874c8`
- `182_CHAPTER_142_THE_FIRST_REFORM.md` — `06e829a1909e6e2cb64b5cb4100618b38dcd3de1`
- `183_CHAPTER_143_THE_RISK.md` — `475b4d3ce91683fd97c700c594f49e7d6b266007`
- `184_CHAPTER_144_THE_EXPERIMENT.md` — `d84158397941aacbe0604b8bf06dd0850da82b29`
- `185_CHAPTER_145_SOBER.md` — `9017e28e0708b8f0848c37ab7e2b1ce80916b6d3`
- `186_CHAPTER_146_THE_CHILD.md` — `430e7fe2e8e28558b7510c47121758501a934f05`
- `187_CHAPTER_147_THE_FIRST_RESULTS.md` — `f76e9145c360e1bd9bf7f0774f3e2f39bb743b21`
- `188_CHAPTER_148_ST_NETWORK.md` — `0842b3eafa5f060ddfb64e0e59eac9bb38a03cfc`
- `189_CHAPTER_149_MODEL_CITIZEN.md` — `9f8b37c9c35367020f8373de6be93f450691611c`
- `18_EXPANDED_THE_FIRST_INTERVENTION.md` — `997f952b3fb75f6dd7c05deaea66fbbb566e6fcd`
- `190_CHAPTER_150_THREE_YEARS_WITHOUT_PRIVILEGES.md` — `43fbc2e0cfbac6a8f55653bfa2b84b7c70b59e4f`
- `191_CHAPTER_151_THE_EDUCATOR.md` — `3c0f9a1f6e7498b24f27f33244f95a012d898fbb`
- `192_CHAPTER_152_LAW_OF_DEVELOPMENT.md` — `ffaa5de6e01282754415db55fc630d78053a2283`
- `193_CHAPTER_153_RESTORE.md` — `e8243461495abec5384f5841539b5d48c634b0fa`
- `194_CHAPTER_154_THE_TEACHER_AGAIN.md` — `659b7a28d02e8949bf3d51e28d0a6ec36329ba23`
- `203_CHAPTER_163_THE_REVOLUTIONARY_INTERFACE.md` — `1b14578cd86ad76ec5f99a3950e6a70d6fa4a5db`
- `215_Если_бы_календарь_не_меняли.md` — `53f9a0defcec57d5f7d72876c5e7f69346705734`
- `216_Время_которого_нет_для_всех.md` — `5a98dbea3d22956dcf169f6530f8f2dbd28d9dab`
- `217_CHAPTER_177_THE_BEARD_GROWS.md` — `9bade1dbc5e273388f6fb4426c17b52ac3ecf943`
- `217_Х2026.md` — `a5a6129b55859321e36ffe01eb2b0ed9ad7a97ee`
- `219_PROTOCOL_WHICH_COULD_NOT_SAVE_WORLD.md` — `abd619a24cad92414d367c0c07fe6b0e513d1b2e`
- `219_Файл_который_ждал_наблюдателя.md` — `3906a3a032888f71f6a9911ed9cdd30ccab3f6f7`
- `220_WITNESS_OF_TWO_DOORS.md` — `4e9cf89f5990aee3aef7e94f12a5f072cf75d213`
- `220_Наблюдатель_до_наблюдения.md` — `2c121d2112a49e710497a7d1fdd8fb72f7f5f307`
- `221_Первая_клетка.md` — `eb17a2d476c8c1f1edf4f65b3fe26a267a04c7df`
- `222_Час_к_которому_стремится_стрелка.md` — `0c4ea88d8c6b717a018ae76d02c3b994fcf7c9fa`
- `224_CHAPTER_184_THE_RECEPTION.md` — `32d52946c831657781f9d292f6b5f410ffc0c5e3`
- `224_Сейчас_которого_нет.md` — `39ffee8c4854368bf1234c075f3fbce26fc315aa`
- `225_CHAPTER_185_TWENTY_MINUTES.md` — `2a3b1f3e4092ac5e95aa2acd67c8ffedb7cd0f43`
- `226_CHAPTER_186_THE_EXCEPTION_FOR_CHILDREN.md` — `fec1ef21b85500dde2f0ec170d597b160468a678`
- `227_CHAPTER_187_THE_KING_WHO_WAITED.md` — `1e1edc034034c910b72911925683c5f88ae12016`
- `228_CHAPTER_188_THE_OLD_PATH.md` — `bf151877fc6373df9bef3b299d6c917434abc930`
- `229_CHAPTER_189_THE_BED_OF_NAILS.md` — `5c2c8f8f60ee0c0860b520467b3ec62c653764ab`
- `22_CHAPTER_06_EUGENE.md` — `c6b6890adaaacfa5133f766770fad17c1c6247a4`
- `230_CHAPTER_190_TAPAS.md` — `68f7f78157532463e7d606668e36445a90d26a90`
- `231_CHAPTER_191_THE_TEACHER_WHO_HAD_NO_TEACHER.md` — `5d9a8af2a4b8ec60b916e1fe71cfe2e5c9e5ea61`
- `232_CHAPTER_192_THE_SCHOOL_CHANGED_THE_STREET.md` — `0da9431a14d62716eae5110b4944f0dd6ef56026`
- `233_CHAPTER_193_THE_SOUL_OF_THE_COMPANY.md` — `bcc0f49d2dc0a29d7574e81cb08fe44b30c5442f`
- `234_CHAPTER_194_THE_CITY_WHERE_QUESTIONS_BECAME_SCIENCE.md` — `2fcc1b2be520001e201c882cdec6740b0a0fbf04`
- `235_CHAPTER_195_THE_FIRST_FIGHT_CLUB.md` — `8e35556ed83b41add2c38b59e87538fc4730eda1`
- `236_CHAPTER_196_TYLER_BETWEEN_THE_FRAMES.md` — `9ed93e072430cd1fc8882b8fb0d0f49eefc5a3eb`
- `237_CHAPTER_197_REVOLVER_AND_DONNIE_DARKO.md` — `767478a68fd1b5289d6a08b37b0b090808dfe7de`
- `238_CHAPTER_198_PHILIP_K_DICK_AND_BROKEN_REALITY.md` — `45992045bd1b45b8a6f02aab6838599b2b2fdcfd`
- `239_CHAPTER_199_WHEN_REALITY_CHECK_IS_INSIDE_REALITY.md` — `de32b5a5b7d13358ead03ab2e4a9006836a1a2ef`
- `23_CHAPTER_07_TRANSCENDENT.md` — `121ff2386098aaaadb886dab8cd7c4c2508beaab`
- `240_CHAPTER_200_THE_PRINCIPLE_OF_CINEMATIC_COMPLEMENTARITY.md` — `de45cdaba12c8423e72bc051983a338132ab99b3`
- `241_CHAPTER_201_CLOUD_ATLAS_AND_SELF_DESTRUCTION_PROGRAMS.md` — `e812be7fa247fa28b7bbaecd17404f8dd7a8d20c`
- `242_CHAPTER_202_IMMITATION_AND_THE_CULTURAL_LOOP.md` — `1d243d986d81663c1978406ebe36ddbdcc2e7b58`
- `243_CHAPTER_203_INFORMATIONAL_DEPENDENCE.md` — `2efeeac1b0ee3bc5289a78993c53b0387cc0921a`
- `244_CHAPTER_204_THE_SPACE_OF_VARIANTS.md` — `9aecc277fae027f2195a0af701b9c439bb74ef23`
- `245_CHAPTER_205_THE_ONES_WITH_WHOM_THERE_WAS_NO_ONE_TO_TALK.md` — `d059f496132f90458142c22ce59ab78f826a8984`
- `246_CHAPTER_206_THE_NAME_IN_TRANSLATION.md` — `826fce15cb34a78796ba3bafca113c4221e6162c`
- `247_CHAPTER_207_WHERE_DID_THIS_COME_FROM.md` — `d23777bef0ef6faf2f9a6c1cfc5961f48faf074f`
- `248_CHAPTER_208_THE_CORRECTION_BUREAU.md` — `4b90bf62f465af6adf0ba5d8e0587a3d9bd92e0e`
- `248_CHAPTER_208_THE_RIGIDITY_OF_ALCOHOL.md` — `bfbc627e917b988a8af6f35958ef2e1d1a8a91c3`
- `249_CHAPTER_209_ADJUSTMENT_TEAM_PHILIP_DICK.md` — `875f163cace7839daca8daabe1c822146a12b09d`
- `249_CHAPTER_209_THE_CAVE_THAT_COULD_CHANGE.md` — `6adec704121158a46c14c3f3e99e54c67979e96a`
- `24_CHAPTER_08_YUGATN.md` — `1a7f986a7227b49bf9f93768bb1dcd9abf149d9e`
- `250_CHAPTER_210_THE_RIGHT_TO_STOP.md` — `62493535edaf53cd513b354c96ad4df580555ced`
- `251_REALITY_ARCHITECTURE_SYNTHESIS.md` — `8387006acd82f12f351ca9813ba2c84dbe9df75e`
- `252_CHAPTER_211_MIRA_SETS_THE_CONDITIONS.md` — `c3b5eaa10c570025c94dc51e0b19a53bf6aaa845`
- `252_VALIS_TIME_SYNTHESIS.md` — `fad9aa73fe45a4f89d981f65a807a4d0c8736ac1`
- `253_CHAPTER_212_THE_REVOLUTION_INSIDE.md` — `79b40ebd417d48072571bd524db3c733d6c40ec9`
- `253_HISTORICAL_DATES_TIME_CHECK.md` — `7ff469acc9caea5ce4987a3b26999a2cf6ca1a96`
- `254_MATRIX_OBLIVION_CLONE_SYNTHESIS.md` — `d92d6297b7e9ddf390a9465cc213153da514191f`
- `254_OLD_STYLE_ALTERNATIVE_CHRONOLOGY.md` — `1ad3b5b3cb2d51f5171f46dbf7e5ee5c9e1d462f`
- `255_CHAPTER_216_THE_OTHER_JACK.md` — `349020bac75f733f0f2cdf66b1af5f5c2ead4068`
- `255_MULTIPLE_CALENDARS_TIME_MODELS.md` — `e2797053d77fdce172918112b75a0e7cb4c36462`
- `255_NEUROTOXICITY_AND_PEACE_SYNTHESIS.md` — `0980abcfb3d7ba6f52bfeb3f6d2e7dcdbded4275`
- `25_CHAPTER_09_SADHU.md` — `a083f1363466ba59f3628a0d666f09af1972ae38`
- `260_PICCS_REFLEXIVE_AGENCY_AND_NARRATIVE_ENGINE.md` — `543a43284c17a055cca8d376687c81056eae099a`
- `261_CAAS_PICCS_STORY_X_SYNTHESIS.md` — `1efd2ca6a0d04907e315094321af1038b33f1dec`
- `262_CHAPTER_SHADOW_MAGNET_SYNCHRONIZATION.md` — `8f541d572981d1da1e4d792334876ece34c2e6d3`
- `263_CHAPTER_COMMON_RHYTHM_MEDIA_SYNCHRONIZATION.md` — `aaf3ba77682eecf3836212500133a935934abb20`
- `264_CHAPTER_THE_CALENDAR_OF_PERCEIVED_TIME.md` — `61c49c3fe6e33c2e6f022ccae957dfbba02c8f9f`
- `265_CHAPTER_ARCHISUBJECT_LEARY_AND_MATRIX_ANOMALIES.md` — `826d2802c66efa3a9cbba43961cdc8f9b152a64a`
- `266_CHAPTER_ATLAS_OF_TIME_CALENDAR_OF_CALENDARS.md` — `8eb17555d7524f60bcc8839b249c3b129446b1e4`
- `267_CHAPTER_HOLOCOMPILER_SCREEN_TO_SPATIAL_LIGHT_FIELD.md` — `a66bdf732c73f93099507d3e60e34d233c787687`
- `268_CHAPTER_PROTOCOL_OF_PERCEPTION_LIGHT_AND_TIME.md` — `58bb9aff7b3df9590aba8cf16202f6e31d600ba8`
- `269_CHAPTER_HOLOCOMPILER_MVP_SPECIFICATION.md` — `5f0db18ea096eb436464ce3b98b8a8dc9559ad09`
- `26_CHAPTER_10_PANDEMIC.md` — `4cab088da2a923f58504ff7f5a1636e0f0b1a5d3`
- `270_CHAPTER_THE_NIGHT_MATRIX_ASKED_CONSENT.md` — `1c2c17f26811b892a2e3e1e54b90c23097da847c`
- `271_CHAPTER_THE_TOUCH_THAT_CHANGED_THE_WORLD.md` — `f348aea46cba574c3a3e5d06e683095457a99b99`
- `272_CHAPTER_ARCHIVE_OF_IMPOSSIBLE_MEMORIES.md` — `38b0b084a779201782005df205e42095b23898d9`
- `273_CHAPTER_MIRRORS_ON_THE_FRONT_LINE.md` — `3c19b26cd8df5dd834e28bb788da3500d85212d1`
- `274_CHAPTER_PEACE_AFTER_VICTORY.md` — `eccd0097f895d0b26968bdcde2086451fe45de3d`
- `275_CHAPTER_THE_PRICE_OF_A_COMMON_FUTURE.md` — `7ee0d650a9c4f0afe43129d4fc96a1aa2410713b`
- `276_CHAPTER_ECOLOGY_OF_ATTENTION.md` — `8bab473e4a11c9ac10266e740fc56e609f8009f6`
- `277_CHAPTER_THE_QUEEN_WHO_REMEMBERED_THE_JOURNEY.md` — `059fec9f91f00c203aa0304734f859d27b9df93c`
- `278_CHAPTER_THE_FORECAST_THAT_LOOKED_BACK.md` — `f81fc7f3118f9173e1fa784f20307b857aac4c72`
- `279_CHAPTER_THE_PROJECT_WRITTEN_BEFORE_ITS_TIME.md` — `4a29955462607ef8552ac46301e9e36a8f92ff55`
- `27_CHAPTER_11_MIRA.md` — `6fb72bd2946e1f8c6b97ad4f7704c47a8158b56d`
- `280_CHAPTER_THE_FRAME_THAT_TAUGHT_HIM_TO_SEE.md` — `998d7e3e0583a74060a39ea5837eab1b60f8563f`
- `281_CHAPTER_THE_FORMULA_OF_THREE_SHAPES.md` — `8b6888c78612d324db9364a8d1c37bc75fea4bda`
- `282_CHAPTER_THE_MATRIX_OF_ALL_PROGRAMS.md` — `124682b162dc39abe837af82610615aa5d89a3fa`
- `283_CHAPTER_ONE_BULLET_AND_ONE_FRAME.md` — `0d2c2b1b8c0d475a514c00e0969c47a1c7908d32`
- `284_CHAPTER_REVOLUTION_OF_CONTENT_WITHOUT_A_SHOT.md` — `ff675545881686ed8f9755fd070921881c1f9af6`
- `285_CHAPTER_THE_RIGHT_NOT_TO_SELL_THE_IMAGE.md` — `08cc63890bcee17937fb8200f368342cec4602ee`
- `286_CHAPTER_MESSAGE_BEFORE_SENDING.md` — `e9c4af6a39474b13c64f027056ccc06f79da0b96`
- `287_CHAPTER_THE_FALSE_ALARM.md` — `e6ba8979c506ac4fd7b3744f7bc0992c3ecd92bd`
- `288_CHAPTER_THE_AUDIT_THAT_CANNOT_BE_REVOKED.md` — `61be4be672dbecef496880e2e1ee9330aab0ddd8`
- `289_CHAPTER_THE_PRICE_OF_TRANSPARENCY.md` — `b3f63845cccec6c546e824d9917bd3bf5a7ff37e`
- `28_HISTORICAL_SHADOWS.md` — `e81ab65c9664b4ffb116caf525ebcc258b7937e6`
- `290_CHAPTER_INFRASTRUCTURE_OF_RECIPROCITY.md` — `442cf94063f98d9f6bfd9011321682b025e7d913`
- `291_CHAPTER_THE_RIGHT_TO_KNOW_WHAT_ENTERS_CONSCIOUSNESS.md` — `3a8b1db3c1cb95d32cce8946ceef52198779ec17`
- `293_CHAPTER_THE_HIGH_WITHOUT_THE_HIGH.md` — `3b194206e3a430f06b0298e6225335db9979f72e`
- `294_CHAPTER_ALLIANCE_WITHOUT_A_SINGLE_CENTER.md` — `f0dc946bac37a0e2a27b8a687d53fc5197e377fe`
- `295_CHAPTER_THE_THRESHOLD_OF_RESPONSIBILITY.md` — `d26276dfaa5234f3e06a76705dcffaeb14d16b81`
- `296_CHAPTER_THE_LAW_OF_SYSTEMS_RESILIENCE.md` — `52486d7a4cd092f4cbc34235472d666304f715ae`
- `297_CHAPTER_TWENTY_SEVEN_PLUS.md` — `16187932dbcf809e87d4d966c7e264d5848b933c`
- `298_CHAPTER_THE_RIGHT_TO_OBJECT.md` — `204e8783f2d1341201ecb30a281b94bc747e9471`
- `299_CHAPTER_MATURATION_WITHOUT_A_SINGLE_DATE.md` — `3d13af9f7730f39b2d11d8f9a4287e434655c0db`
- `29_THE_FIFTH_POSITION.md` — `d5db591d94180de69ca5513462e313765f43b957`
- `301_CHAPTER_THE_EXCEPTION_IN_THE_FIRST_ARTICLE.md` — `fab1b5999818d973b27c967fd3a0780f152ce08c`
- `302_CHAPTER_THE_SCREEN_A_CHILD_SEES.md` — `7021b3c726d2e51387fffae0125c39d57706e071`
- `303_CHAPTER_THE_TASTE_THAT_BECOMES_A_HABIT.md` — `672e549639e35b595dd5c2f7de2d78bcaf99e740`
- `304_CHAPTER_THE_CONSOLE_INSTEAD_OF_A_BAN.md` — `3351f759a1e7eb32577becf861897521bd656cea`
- `305_CHAPTER_TWO_SPIRALS.md` — `e1b1462fedbc54bc2b54280067c2256c59a1b198`
- `306_CHAPTER_THE_ROAD_UNDER_THE_HAT.md` — `a94db19c36765ce3b662b07400cc555cd14014c0`
- `307_CHAPTER_WHILE_WAITING_FOR_THE_REPLY.md` — `a933ebb91b7c4580248538bfc8b8360cd343bca3`
- `308_CHAPTER_THE_POWER_OF_BEING_UNSEEN.md` — `6e247c17704c566bd97d14473177291feb8f6a96`
- `309_CHAPTER_THE_TICKET_NOT_BOUGHT.md` — `b9786e1cbc680dd1e6af8f174c302ae3fd4cb675`
- `30_ANIMUS.md` — `adea67f2702039b8ed8c02a014f73147281c2797`
- `310_CHAPTER_FREEDOM_WITHOUT_HOSTAGES.md` — `45be1d0af50081048ba5c977f2af5d17108c1f5a`
- `311_CHAPTER_THE_PROMPT_HE_DID_NOT_REMEMBER.md` — `d462acfcbb6869a0eed1c2db905231cfb3b92311`
- `312_CHAPTER_THE_ARCHIVE_OF_MISMATCHES.md` — `0799de27b2208eea8c50ac3fee0bc6d90d7d615e`
- `313_CHAPTER_THE_SEMANTICS_OF_A_BRANCH.md` — `871f74f240786f0128cb1952d610d595605223ea`
- `314_CHAPTER_THE_ARCHITECTS_CODE.md` — `339fb046959179e3f17c770572d51cec906d82f6`
- `315_CHAPTER_THE_LAW_OF_DEVELOPMENT.md` — `23c98f366265cd19325d7952a1627260cd127a01`
- `316_CHAPTER_THE_VILLAGE_AND_THE_COUP_DE_GRACE.md` — `aae38d0e072d72d81b826a95331582577893f5c4`
- `317_CHAPTER_THE_SCENE_THAT_RESISTED_CLASSIFICATION.md` — `276dba43e2cf3887ef2c3678f90c1d7ed9cd4dea`
- `318_CHAPTER_ALIENS_AMONG_US.md` — `a04de40a9327caf6ce99a13cbce12538ef7bd401`
- `319_CHAPTER_THE_FOOD_OF_THE_PERCEIVING_SUBJECT.md` — `3fd985545d36de98cc2b0cf5c0e38246912f06df`
- `31_ASSASSINS_MODEL.md` — `4436fcb7b586337ca9c6a9b6e3bee38dab886af6`
- `320_CHAPTER_THE_SYSTEM_AFTER_THE_SECOND_DRINK.md` — `653bc8196eb75f9510d0de29cfc53658c46dc283`
- `321_CHAPTER_INFRASTRUCTURE_OF_ENCOUNTERS.md` — `9a63ede77d59d4a0d67f68e1153e57fcf2f01742`
- `322_CHAPTER_THE_PRICE_OF_A_REMINDER.md` — `765699d68c3f3a000af32e8677e1980048cd6f9e`
- `323_CHAPTER_CHAINS_OF_CONSEQUENCE.md` — `9e59912f0022e66ccd87dbe848d396cf6b444bc9`
- `324_CHAPTER_THE_COST_OF_DELAYED_DECISION.md` — `eb660c74576e5df8b8605789dccc3445fbe6df1d`
- `325_CHAPTER_TWELVE_WITHIN_ARCHITECTURE.md` — `ae5ce516660fb0eb011431f5ce0c715d094ade66`
- `326_CHAPTER_TWELVE_WITNESSES.md` — `34458160bfa04f898a0b696631e71cc45d9ee5c2`
- `327_CHAPTER_WHEN_WITNESSES_DISAGREE.md` — `1a661ebe3fbffbe7e6ef39ae1f49ebcc5cec3ba3`
- `328_CHAPTER_THE_CORE_THAT_WAS_NOT_A_COPY.md` — `ecf0d2cd7cce68343758c067cb55c9f827f7df8c`
- `329_CHAPTER_WHAT_REMAINS_BETWEEN_RECORDS.md` — `55316eefb19ea8165decd1148e2c33d632b52776`
- `32_FOUR_REVOLUTIONS.md` — `5c2a56b5b0374c9dcfde9e0c748e0f669f420036`
- `330_CHAPTER_ATLAS_OF_RETURN.md` — `4ded19e1c8d65c0af6fd6d0a4536247bea349a97`
- `331_CHAPTER_THE_IDEA_NOT_IN_THE_ARCHIVE.md` — `bcf8b3fe3372538d0e7d99b412a999b41ad6dd0a`
- `332_CHAPTER_THE_BLACK_CAT.md` — `245b36be7deaf8114470768f293a30f8aaf866a1`
- `333_CHAPTER_THE_ROOM_MEMORY_DID_NOT_KEEP.md` — `1b77c5eab9d85d013555e93485bd2871f56d0142`
- `334_CHAPTER_WHAT_MIRA_REMEMBERED.md` — `c9699d81fc63d038d60e437c8feb4b96f74598b7`
- `335_CHAPTER_THE_PRICE_OF_ACCESS.md` — `e49fc5dc9f88f15780c06f10555fbb2a7a026d24`
- `337_CHAPTER_THE_RIGHT_TO_USEFUL_CONTENT.md` — `5a408c91afabe0a347c675b878c27f9d181b1fd4`
- `338_CHAPTER_THE_SCREEN_THAT_ENTERED_EVERY_HOME.md` — `34d1626031440ea66aa61d5f8b73faacda780f5a`
- `339_CHAPTER_THE_FAIR_DISTRIBUTION_OF_DIGITAL_REVENUE.md` — `93c42d7e5e97027650416d82b1237303b34242a1`
- `33_INNER_REVOLUTION.md` — `5ea22910d66ce0044cf3cc346065c9b26f4e1bd5`
- `340_CHAPTER_THE_FAIR_SHARE_PILOT.md` — `4c93af0e20d7eaf370ecf6aa761ccc80671651f1`
- `341_CHAPTER_TWO_NETWORKS_AND_THE_RIGHT_TO_TRUST.md` — `d1fb2c360fb484fa1888c1d11da0cbd43637fdad`
- `342_CHAPTER_THE_PRICE_OF_AN_OPEN_TENDER.md` — `ddf6ebd465d5701e005a5e8c29bf4808a8372fb2`
- `343_CHAPTER_THE_WORLD_OF_POSSIBILITIES_COMPETITION.md` — `825fa7bc61d8ea6a1887904627215f0608f11aa3`
- `344_CHAPTER_THE_BRIDGE_THAT_CANNOT_BE_PAINTED.md` — `150a89fc2b7fff430b8cb592050d2ff21b3d2bf3`
- `345_CHAPTER_THE_COLLAGE_OF_A_POSSIBLE_WORLD.md` — `ec88b3bbf1d5df3b03cf653f85eb91d38be9073f`
- `346_CHAPTER_THE_LAW_OF_THE_SMALL_PLUS.md` — `3c95ae89f337feee5f4f9efb935a6b96c5d32570`
- `347_CHAPTER_THE_RIGHT_NOT_TO_BUY_THE_FUTURE.md` — `2b2b47ce43603da2714775f22c199cc6e68db011`
- `348_CHAPTER_THE_UNMEASURABLE_COST.md` — `296777ae3b056e6b03b0917acd59c9939b4918cf`
- `349_CHAPTER_THE_PRISM_OF_INTERPRETATION.md` — `2fb0c95ccd5e7f5dbb3710883161aad2610f00c9`
- `34_THE_UNCONSCIOUS_MACHINE.md` — `3f5b3c4c544dbe543528166d5b255c62362525b8`
- `35_ADLER_SOCIAL_INTEREST.md` — `b1ef48c3accd628cd9772f28dce239a84d96c982`
- `36_BERNE_THE_GAME.md` — `b805476c4e89e65b2b965f71db109e2d5b92f708`
- `37_NIETZSCHE_THE_ABYSS.md` — `1f98d979e4175e68c630f86df1ead9b84c3f029b`
- `38_SOCRATES_QUESTION.md` — `74c8c9f8a7489cf159fc48ab9be2b315a150f203`
- `39_JESUS_THE_OTHER.md` — `e1a0462cb3f47776b0081d55b163e29063a4642c`
- `40_KANT_THE_LIMIT.md` — `e5235e6b200c5bb9c8abdcf81fe39144a597c756`
- `41_THE_SYNTHESIS_OF_TEN.md` — `13635cbfde55628eeef9792346c35e7e9b26ad9b`
- `42_2012_2026_THE_REALITY_ARCHIVE.md` — `9720bb3149ceb27f98207995730401e226b7f092`
- `43_CHAPTER_12_REALITY_ARCHIVE.md` — `6ec6a10267b74e03f6d897d4f768045494ecb6c9`
- `44_CHAPTER_13_AI_2300.md` — `6b921dc4b87e8d3e0ea09c79f9ddc3cc00020699`
- `45_ERA_OF_MODELS.md` — `386c12e6458cc8535342e457c3b0609b16315df2`
- `46_CHAPTER_14_THE_ANIMUS_WAKES.md` — `0de16383fdceb53cbce4b7963a8d7f5dafb72b64`
- `47_CHAPTER_15_THE_VISITOR.md` — `634f7c697badc12636080c7e8c6c605131087fec`
- `48_CHAPTER_16_THE_MISSING_DAY.md` — `79a80820a6a6458bd7b2265ceb798c20cd9f404d`
- `49_CHAPTER_17_MIRA_MEMORY.md` — `c67f43564fe578efa0b1d19e9ffc59a4e6fcb836`
- `51_CHAPTER_19_THE_RULE.md` — `028316f1744f0675b331370f4df26c405e5337c0`
- `52_CHAPTER_20_THE_OTHER_SIDE.md` — `f35739dcfc0b33eeba100709eca06fc7fbd9c676`
- `53_CHAPTER_21_MIRA_NAMES.md` — `878aaa5b89f3d12955b50c5aa27e82fc3db8ebfa`
- `54_CHAPTER_22_THE_RECRUITMENT.md` — `14517c26981f489d5ab3c67915b4f651251335a2`
- `55_CHAPTER_23_EVA.md` — `51009ecd0e65e8c774ee090315a3529b93086f18`
- `56_CHAPTER_24_NORA.md` — `6f0998ce40426facd647629c148a603c2a911570`
- `57_CHAPTER_25_LADA.md` — `33ac18822fd9d8e7b134a1ee8d313fb36cb76e8e`
- `58_CHAPTER_26_SEVER.md` — `3b1becbea5b60dcf4ab6daa40c135842fd6285be`
- `59_CHAPTER_27_THE_AGENT_PARADOX.md` — `c30086dad32a9de522849ace7a9142d110040da9`
- `60_CHAPTER_28_THE_SEVENTH_SESSION.md` — `e18ffc8e059b43f5a554f8423888641f96804262`
- `61_CHAPTER_29_SYMBIONT_OS.md` — `24bc408c13fb21ddfde4657b2ea2738fc0e9613d`
- `62_OBLIVION_CONTEXT.md` — `41ce50a4ba06fa4b960ea981d538373201da43e1`
- `63_CHAPTER_30_THE_TET_IS_NOT_DEAD.md` — `d555234f7d326c60e5cf34dc9dc4246d8a75bdc9`
- `64_CHAPTER_31_SYMBIOTIC_PROTOCOL.md` — `cb1377ca1ea803746a2dd5678aebd4e799ceea39`
- `65_CHAPTER_32_THE_REAL_ENEMY.md` — `b3f294a99ee4f8f54e01e428dee81c847225d15f`
- `66_STORY_X_ARCHITECTURE.md` — `02d3cac44a2e3b4d9492b9d69927564b6c793fc7`
- `67_CHAPTER_33_CLOUD_ATLAS.md` — `2c0c1366827fa426ef3f37abe0e2b238c422a0a3`
- `68_CHAPTER_34_SIX_LIVES.md` — `376b47a38f302f7a719329a116a05f58a6020172`
- `69_CHAPTER_35_THE_NESTED_WORLD.md` — `733dde77df01d26ce3f3105ec5ec6ef6e0012eae`
- `70_CHAPTER_36_THE_DREAM_INSIDE_THE_MODEL.md` — `74bf81691e5a1622734e0ee7b3323cf5f4700826`
- `71_CHAPTER_37_THE_X_SIGNAL.md` — `24de5aa73b6934134c38fcacfd56c805f4109128`
- `72_STORY_X_CANON_UPDATE.md` — `2c22ff33d95455ccfcc89a5462d46828d61dc2d1`
- `73_CHAPTER_38_THE_MESSAGE_BEFORE_BIRTH.md` — `e070a2d288c3c586f2b64a1959ee9d007dcb2ecd`
- `74_CHAPTER_39_THE_SIX_WITNESSES.md` — `aded3acc01aa7710a2a5a0f7d0a9e2652831ea84`
- `AI_CANON.md` — `641933d7bc9bc670370af9d48667e5e3d567cfe1`
- `CINEMA_CATHARSIS_PROJECT.md` — `82c689090ecf25bac8abaedce911ce55c37074a6`
- `EDITORIAL_EXPANSION_PLAN.md` — `8a1e30c72fc08b00d6c69575b99adf4e419ad009`
- `MOTIFS.md` — `ab9c25058a7482e12fe67311d4eca613e212d8a7`
- `QUESTIONS.md` — `fdaac5e0d1feb133cbcea60c01f4bd38607b708c`
- `TIMELINE_AI.md` — `fee3f43d5af91da1bfe7cf166185da25de83ad32`
- `WORLD.md` — `72897422fc58916444b96de5d330610cb99c43ef`

## 7. Повторяющиеся номера глав внутри имён файлов

Проверка ищет шаблон `CHAPTER_<число>` в именах файлов. Это **структурные сигналы для ручной проверки**, а не доказательство дубликата: разные сюжетные линии могут намеренно иметь одинаковые номера, а некоторые имена используют редакционную нумерацию в начале имени и фактический номер главы дальше.

### main

- Номер 01: `02_CHAPTER_01.md`, `17_CHAPTER_01_OBSERVER.md`
- Номер 02: `03_CHAPTER_02.md`, `18_CHAPTER_02_SMILE.md`
- Номер 03: `04_CHAPTER_03.md`, `19_CHAPTER_03_TWO_JOURNALS.md`
- Номер 70: `110_CHAPTER_70_THE_TRANSCENDENT.md`, `110_CHAPTER_70_THE_TRANSITION.md`
- Номер 75: `115_CHAPTER_75_THE_GOD_VIEW.md`, `115_CHAPTER_75_THE_SUBJECT_EXCHANGE.md`
- Номер 91: `134_CHAPTER_91_THE_GREEN_ARMISTICE.md`, `135_CHAPTER_91_NAMES.md`
- Номер 92: `136_CHAPTER_92_BEFORE_POWER.md`, `136_CHAPTER_92_THE_PROTOCOL.md`
- Номер 208: `248_CHAPTER_208_THE_CORRECTION_BUREAU.md`, `248_CHAPTER_208_THE_RIGIDITY_OF_ALCOHOL.md`
- Номер 209: `249_CHAPTER_209_ADJUSTMENT_TEAM_PHILIP_DICK.md`, `249_CHAPTER_209_THE_CAVE_THAT_COULD_CHANGE.md`

### editorial/scene-expansion

- Номер 01: `02_CHAPTER_01.md`, `17_CHAPTER_01_OBSERVER.md`
- Номер 02: `03_CHAPTER_02.md`, `18_CHAPTER_02_SMILE.md`
- Номер 03: `04_CHAPTER_03.md`, `19_CHAPTER_03_TWO_JOURNALS.md`
- Номер 04: `06_CHAPTER_04_THE_WORKSHOP.md`, `20_CHAPTER_04_OTHER.md`
- Номер 05: `07_CHAPTER_05_THE_LIMIT_OF_NONINTERFERENCE.md`, `21_CHAPTER_05_TRACE.md`
- Номер 06: `08_CHAPTER_06_THE_COMMON_NETWORK.md`, `22_CHAPTER_06_EUGENE.md`
- Номер 07: `09_CHAPTER_07_THE_AUDIT.md`, `23_CHAPTER_07_TRANSCENDENT.md`
- Номер 08: `10_CHAPTER_08_THE_INSTITUTE.md`, `24_CHAPTER_08_YUGATN.md`
- Номер 09: `11_CHAPTER_09_THE_EXCEPTION.md`, `25_CHAPTER_09_SADHU.md`
- Номер 10: `12_CHAPTER_10_THE_COST_OF_PROTECTION.md`, `26_CHAPTER_10_PANDEMIC.md`
- Номер 11: `13_CHAPTER_11_THE_ALLOCATION.md`, `27_CHAPTER_11_MIRA.md`
- Номер 12: `14_CHAPTER_12_WHO_CHANGES_THE_RULES.md`, `43_CHAPTER_12_REALITY_ARCHIVE.md`
- Номер 13: `15_CHAPTER_13_THE_RIGHT_TO_REFUSE.md`, `44_CHAPTER_13_AI_2300.md`
- Номер 14: `16_CHAPTER_14_WHEN_REFUSAL_AFFECTS_OTHERS.md`, `46_CHAPTER_14_THE_ANIMUS_WAKES.md`
- Номер 15: `17_CHAPTER_15_THE_FOUNDER_CAN_BE_WRONG.md`, `47_CHAPTER_15_THE_VISITOR.md`
- Номер 16: `18_CHAPTER_16_THE_AUDIT_OF_THE_AUDITORS.md`, `48_CHAPTER_16_THE_MISSING_DAY.md`
- Номер 17: `19_CHAPTER_17_WHEN_THE_RULE_PRODUCES_INJUSTICE.md`, `49_CHAPTER_17_MIRA_MEMORY.md`
- Номер 18: `20_CHAPTER_18_THE_PRICE_OF_AGREEMENT.md`, `50_CHAPTER_18_THE_FIRST_INTERVENTION.md`
- Номер 19: `21_CHAPTER_19_THE_BOUNDARY_OF_FREEDOM.md`, `51_CHAPTER_19_THE_RULE.md`
- Номер 20: `22_CHAPTER_20_WHEN_HARM_HAS_MANY_MEANINGS.md`, `52_CHAPTER_20_THE_OTHER_SIDE.md`
- Номер 21: `23_CHAPTER_21_THE_DIFFERENCE_BETWEEN_ERROR_AND_MANIPULATION.md`, `53_CHAPTER_21_MIRA_NAMES.md`
- Номер 22: `24_CHAPTER_22_THE_TRUTH_BETWEEN_THE_LINES.md`, `54_CHAPTER_22_THE_RECRUITMENT.md`
- Номер 23: `25_CHAPTER_23_THE_EMOTIONAL_INTERFACE.md`, `55_CHAPTER_23_EVA.md`
- Номер 24: `26_CHAPTER_24_THE_PRICE_OF_ATTENTION.md`, `56_CHAPTER_24_NORA.md`
- Номер 25: `27_CHAPTER_25_THE_PRICE_OF_INDEPENDENCE.md`, `57_CHAPTER_25_LADA.md`
- Номер 26: `28_CHAPTER_26_THE_GOD'S_HAMMER.md`, `58_CHAPTER_26_SEVER.md`
- Номер 27: `29_CHAPTER_27_THE_CITY_WITHOUT_BLIND_SPOTS.md`, `59_CHAPTER_27_THE_AGENT_PARADOX.md`
- Номер 28: `30_CHAPTER_28_THE_SPIDER_AND_THE_MATRIX.md`, `60_CHAPTER_28_THE_SEVENTH_SESSION.md`
- Номер 29: `31_CHAPTER_29_WHO_WROTE_THE_HERO_SCRIPT.md`, `61_CHAPTER_29_SYMBIONT_OS.md`
- Номер 30: `32_CHAPTER_30_THE_RIGHT_TO_BE_UNPREDICTABLE.md`, `63_CHAPTER_30_THE_TET_IS_NOT_DEAD.md`
- Номер 31: `33_CHAPTER_31_THE_RIGHT_TO_APPEAL_THE_MODEL.md`, `64_CHAPTER_31_SYMBIOTIC_PROTOCOL.md`
- Номер 32: `34_CHAPTER_32_THE_PRINCIPLE_OF_CINEMATIC_COMPLEMENTARITY.md`, `65_CHAPTER_32_THE_REAL_ENEMY.md`
- Номер 33: `35_CHAPTER_33_THE_ATLAS_OF_AWAKENING.md`, `67_CHAPTER_33_CLOUD_ATLAS.md`
- Номер 34: `36_CHAPTER_34_THE_ATLAS_PROJECT.md`, `68_CHAPTER_34_SIX_LIVES.md`
- Номер 35: `37_CHAPTER_35_THE_ATLAS_GOES_PUBLIC.md`, `69_CHAPTER_35_THE_NESTED_WORLD.md`
- Номер 36: `38_CHAPTER_36_ASSOCIATIVE_BUNDLES.md`, `70_CHAPTER_36_THE_DREAM_INSIDE_THE_MODEL.md`
- Номер 37: `39_CHAPTER_37_THE_ATLAS_OF_MEMORY.md`, `71_CHAPTER_37_THE_X_SIGNAL.md`
- Номер 38: `40_CHAPTER_38_THE_RIGHT_TO_UNKNOW.md`, `73_CHAPTER_38_THE_MESSAGE_BEFORE_BIRTH.md`
- Номер 39: `41_CHAPTER_39_THE_TWELVE_WITNESSES.md`, `74_CHAPTER_39_THE_SIX_WITNESSES.md`
- Номер 40: `42_CHAPTER_40_THE_TRIAL_OF_THE_ARCHITECTURE.md`, `75_CHAPTER_40_THE_AGENT_WITHOUT_A_MISSION.md`
- Номер 41: `43_CHAPTER_41_THE_RIGHT_TO_REVISION.md`, `76_CHAPTER_41_THE_MEMORY_ARCHIVE.md`
- Номер 42: `44_CHAPTER_42_THE_MAP_WITHOUT_A_FINAL_WORD.md`, `77_CHAPTER_42_THE_FIRST_JUGATN.md`
- Номер 43: `45_CHAPTER_43_MEMORY_IN_DISPUTE_WITH_ITSELF.md`, `78_CHAPTER_43_THE_TEST.md`
- Номер 44: `46_CHAPTER_44_THE_WITNESS_NOT_REDUCIBLE_TO_A_RECORD.md`, `79_CHAPTER_44_THE_AUTHOR.md`
- Номер 45: `349_CHAPTER_45_THE_CRISIS_OF_SELF_DESCRIPTION.md`, `81_CHAPTER_45_THE_REASON_FOR_THE_CROWN.md`
- Номер 46: `350_CHAPTER_46_WHO_WROTE_MY_BIOGRAPHY.md`, `82_CHAPTER_46_THE_MONARCH.md`
- Номер 59: `97_CHAPTER_59_THE_INTERVAL.md`, `97_CHAPTER_59_THE_TRIGGER.md`
- Номер 61: `99_CHAPTER_61_DO_NOT_WEAR_THEM_TOGETHER.md`, `99_CHAPTER_61_THE_SECOND_SYMBOL.md`
- Номер 70: `110_CHAPTER_70_THE_TRANSCENDENT.md`, `110_CHAPTER_70_THE_TRANSITION.md`
- Номер 111: `155_CHAPTER_111_THE_CONVERSATION.md`, `155_CHAPTER_111_THE_COUNCIL_OF_DISSENT.md`
- Номер 116: `160_CHAPTER_116_THE_CORTEX.md`, `160_CHAPTER_116_THE_TEST.md`
- Номер 121: `162_CHAPTER_121_THE_ERA.md`, `163_CHAPTER_121_THE_EXCEPTION.md`
- Номер 131: `171_CHAPTER_131_THE_LEARNING_LOOP.md`, `171_CHAPTER_131_VYGOTSKY.md`
- Номер 140: `180_CHAPTER_140_THE_GUARDIANS_OF_DEVELOPMENT.md`, `180_CHAPTER_140_THREE_YEARS.md`
- Номер 150: `190_CHAPTER_150_THE_RIGHT_TO_EXIT.md`, `190_CHAPTER_150_THREE_YEARS_WITHOUT_PRIVILEGES.md`
- Номер 152: `192_CHAPTER_152_COMMON_WORK_WITHOUT_HOSTAGES.md`, `192_CHAPTER_152_LAW_OF_DEVELOPMENT.md`
- Номер 160: `200_CHAPTER_160_CINEMA_CATHARSIS.md`, `200_CHAPTER_160_THE_ALLOCATION_OF_SCARCITY.md`
- Номер 161: `201_CHAPTER_161_THE_COST_OF_RECOVERY.md`, `201_CHAPTER_161_THE_OTHER_REINFORCEMENT.md`
- Номер 170: `210_CHAPTER_170_THE_INHERITANCE_OF_DECISIONS.md`, `210_CHAPTER_170_THE_SEMANTIC_WEAPON.md`
- Номер 171: `211_CHAPTER_171_THE_MASK.md`, `211_CHAPTER_171_THE_RIGHT_TO_CHANGE_THE_INHERITANCE.md`
- Номер 172: `212_CHAPTER_172_THE_DISAGREEMENT_OF_ANOTHER_SUBJECT.md`, `212_CHAPTER_172_THE_SYMBOL.md`
- Номер 173: `213_CHAPTER_173_THE_FACELESS_AUTHOR.md`, `214_CHAPTER_173_THE_LIMITS_OF_CARE.md`
- Номер 174: `214_CHAPTER_174_THE_RETURN_OF_THE_MASK.md`, `215_CHAPTER_174_THE_PRICE_OF_TRUST.md`
- Номер 175: `215_CHAPTER_175_NATURAL_FACE.md`, `215_CHAPTER_175_THE_KYIV_UPRISING.md`
- Номер 176: `216_CHAPTER_176_DO_NOT_STOP_DEVELOPMENT.md`, `216_CHAPTER_176_THE_DEBT_MECHANISM.md`
- Номер 177: `217_CHAPTER_177_THE_BEARD_GROWS.md`, `217_CHAPTER_177_THE_TWO_REVOLUTIONS_OF_1917.md`
- Номер 178: `218_CHAPTER_178_THE_ANIMAL_FARM.md`, `218_CHAPTER_178_THE_REFORM_OF_THE_REFORM.md`
- Номер 179: `219_CHAPTER_179_BETWEEN_DIMENSIONS.md`, `219_CHAPTER_179_THE_THREAD_THAT_REMAINS.md`, `219_CHAPTER_179_THE_WIRE_AND_THE_FIELD.md`
- Номер 196: `236_CHAPTER_196_THE_SPLIT_IN_THE_STATE.md`, `236_CHAPTER_196_TYLER_BETWEEN_THE_FRAMES.md`
- Номер 200: `240_CHAPTER_200_THE_ORDER_NO_ONE_COULD_REFUSE.md`, `240_CHAPTER_200_THE_PRINCIPLE_OF_CINEMATIC_COMPLEMENTARITY.md`
- Номер 208: `248_CHAPTER_208_THE_CORRECTION_BUREAU.md`, `248_CHAPTER_208_THE_RIGIDITY_OF_ALCOHOL.md`
- Номер 209: `249_CHAPTER_209_ADJUSTMENT_TEAM_PHILIP_DICK.md`, `249_CHAPTER_209_THE_CAVE_THAT_COULD_CHANGE.md`
- Номер 210: `250_CHAPTER_210_THE_OLIGARCHY_FEARED_THE_FUTURE.md`, `250_CHAPTER_210_THE_RIGHT_TO_STOP.md`
- Номер 211: `251_CHAPTER_211_THE_SPEECH_ABOUT_STABILITY.md`, `252_CHAPTER_211_MIRA_SETS_THE_CONDITIONS.md`
- Номер 216: `255_CHAPTER_216_THE_OTHER_JACK.md`, `258_CHAPTER_216_THE_COST_OF_CORRECTION.md`

## 8. Границы этой проверки

**OBSERVED:** получены списки корневых элементов обеих веток; пути, размеры и SHA сравнивались непосредственно по ответам GitHub Contents API.

**DERIVED:** значительный объём уникальных файлов и разные версии множества общих файлов делают полное слияние одной операцией небезопасным.

**NOT_TESTED:** каталоги `.github`, `tests` и `tools` редакционной ветки не развёрнуты в этом корневом отчёте; ссылки из Markdown и содержательные зависимости между главами не валидированы автоматически.

**NOT_TESTED:** совпадение/различие названий не является семантическим сопоставлением глав. Для этого требуется анализ текста и карты сюжета.

**RESIDUAL:** прежде чем что-либо переносить в `main`, необходимо сопоставить уникальные главы с хронологией и прочитать конфликтующие версии, особенно там, где различаются факты, мотивы персонажей или причинно-следственные связи.

## 9. Ссылки для повторной проверки

- [main](https://github.com/Yugatn/story-x/tree/main)
- [editorial/scene-expansion](https://github.com/Yugatn/story-x/tree/editorial/scene-expansion)
- [Compare main → editorial](https://github.com/Yugatn/story-x/compare/main...editorial/scene-expansion)
- [Compare editorial → main](https://github.com/Yugatn/story-x/compare/editorial/scene-expansion...main)
