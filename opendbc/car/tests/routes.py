from typing import NamedTuple

from opendbc.car.chrysler.values import CAR as CHRYSLER
from opendbc.car.gm.values import CAR as GM
from opendbc.car.ford.values import CAR as FORD
from opendbc.car.honda.values import CAR as HONDA
from opendbc.car.hyundai.values import CAR as HYUNDAI
from opendbc.car.nissan.values import CAR as NISSAN
from opendbc.car.mazda.values import CAR as MAZDA
from opendbc.car.mock.values import CAR as MOCK
from opendbc.car.subaru.values import CAR as SUBARU
from opendbc.car.toyota.values import CAR as TOYOTA
from opendbc.car.values import Platform
from opendbc.car.volkswagen.values import CAR as VOLKSWAGEN
from opendbc.car.body.values import CAR as COMMA

# FIXME: add routes for these cars
non_tested_cars = [
  MOCK.MOCK,
  FORD.FORD_F_150_MK14,
  GM.CADILLAC_ATS,
  GM.HOLDEN_ASTRA,
  GM.CHEVROLET_MALIBU,
  HYUNDAI.GENESIS_G90,
  HONDA.HONDA_ODYSSEY_CHN,
  VOLKSWAGEN.VOLKSWAGEN_CRAFTER_MK2,  # need a route from an ACC-equipped Crafter
  SUBARU.SUBARU_FORESTER_HYBRID,
]


class CarTestRoute(NamedTuple):
  route: str
  car_model: Platform | None
  segment: int | None = None


routes = [
  CarTestRoute("efdf9af95e71cd84|2022-05-13--19-03-31", COMMA.COMMA_BODY),

  CarTestRoute("0c94aa1e1296d7c6|2021-05-05--19-48-37", CHRYSLER.JEEP_GRAND_CHEROKEE),
  CarTestRoute("91dfedae61d7bd75|2021-05-22--20-07-52", CHRYSLER.JEEP_GRAND_CHEROKEE_2019),
  CarTestRoute("420a8e183f1aed48|2020-03-05--07-15-29", CHRYSLER.CHRYSLER_PACIFICA_2018_HYBRID),  # 2017
  CarTestRoute("43a685a66291579b|2021-05-27--19-47-29", CHRYSLER.CHRYSLER_PACIFICA_2018),
  CarTestRoute("378472f830ee7395|2021-05-28--07-38-43", CHRYSLER.CHRYSLER_PACIFICA_2018_HYBRID),
  CarTestRoute("8190c7275a24557b|2020-01-29--08-33-58", CHRYSLER.CHRYSLER_PACIFICA_2019_HYBRID),
  CarTestRoute("3d84727705fecd04|2021-05-25--08-38-56", CHRYSLER.CHRYSLER_PACIFICA_2020),
  CarTestRoute("221c253375af4ee9|2022-06-15--18-38-24", CHRYSLER.RAM_1500_5TH_GEN),
  CarTestRoute("8fb5eabf914632ae|2022-08-04--17-28-53", CHRYSLER.RAM_HD_5TH_GEN, segment=6),
  CarTestRoute("3379c85aeedc8285|2023-12-07--17-49-39", CHRYSLER.DODGE_DURANGO),

  CarTestRoute("54827bf84c38b14f|2023-01-25--14-14-11", FORD.FORD_BRONCO_SPORT_MK1),
  CarTestRoute("f8eaaccd2a90aef8|2023-05-04--15-10-09", FORD.FORD_ESCAPE_MK4),
  CarTestRoute("62241b0c7fea4589|2022-09-01--15-32-49", FORD.FORD_EXPLORER_MK6),
  CarTestRoute("e886087f430e7fe7|2023-06-16--23-06-36", FORD.FORD_FOCUS_MK4),
  CarTestRoute("bd37e43731e5964b|2023-04-30--10-42-26", FORD.FORD_MAVERICK_MK1),
  CarTestRoute("112e4d6e0cad05e1|2023-11-14--08-21-43", FORD.FORD_F_150_LIGHTNING_MK1),
  CarTestRoute("83a4e056c7072678|2023-11-13--16-51-33", FORD.FORD_MUSTANG_MACH_E_MK1),
  CarTestRoute("37998aa0fade36ab/00000000--48f927c4f5", FORD.FORD_RANGER_MK2),
  #TestRoute("f1b4c567731f4a1b|2018-04-30--10-15-35", FORD.FUSION),

  CarTestRoute("7cc2a8365b4dd8a9|2018-12-02--12-10-44", GM.GMC_ACADIA),
  CarTestRoute("aa20e335f61ba898|2019-02-05--16-59-04", GM.BUICK_REGAL),
  CarTestRoute("75a6bcb9b8b40373|2023-03-11--22-47-33", GM.BUICK_LACROSSE),
  CarTestRoute("e746f59bc96fd789|2024-01-31--22-25-58", GM.CHEVROLET_EQUINOX),
  CarTestRoute("ef8f2185104d862e|2023-02-09--18-37-13", GM.CADILLAC_ESCALADE),
  CarTestRoute("46460f0da08e621e|2021-10-26--07-21-46", GM.CADILLAC_ESCALADE_ESV),
  CarTestRoute("168f8b3be57f66ae|2023-09-12--21-44-42", GM.CADILLAC_ESCALADE_ESV_2019),
  CarTestRoute("c950e28c26b5b168|2018-05-30--22-03-41", GM.CHEVROLET_VOLT),
  CarTestRoute("f08912a233c1584f|2022-08-11--18-02-41", GM.CHEVROLET_BOLT_EUV, segment=1),
  CarTestRoute("555d4087cf86aa91|2022-12-02--12-15-07", GM.CHEVROLET_BOLT_EUV, segment=14),  # Bolt EV
  CarTestRoute("38aa7da107d5d252|2022-08-15--16-01-12", GM.CHEVROLET_SILVERADO),
  CarTestRoute("5085c761395d1fe6|2023-04-07--18-20-06", GM.CHEVROLET_TRAILBLAZER),
  CarTestRoute("162796f1469f2f1b/00000005--6f334eda14", GM.CADILLAC_XT4),
  CarTestRoute("477dd485611d1e6e/00000009--85fc06e10a", GM.CHEVROLET_VOLT_2019),

  CarTestRoute("0e7a2ba168465df5|2020-10-18--14-14-22", HONDA.ACURA_RDX_3G),
  CarTestRoute("a74b011b32b51b56|2020-07-26--17-09-36", HONDA.HONDA_CIVIC),
  CarTestRoute("a859a044a447c2b0|2020-03-03--18-42-45", HONDA.HONDA_CRV_EU),
  CarTestRoute("68aac44ad69f838e|2021-05-18--20-40-52", HONDA.HONDA_CRV),
  CarTestRoute("14fed2e5fa0aa1a5|2021-05-25--14-59-42", HONDA.HONDA_CRV_HYBRID),
  CarTestRoute("52f3e9ae60c0d886|2021-05-23--15-59-43", HONDA.HONDA_FIT),
  CarTestRoute("2c4292a5cd10536c|2021-08-19--21-32-15", HONDA.HONDA_FREED),
  CarTestRoute("03be5f2fd5c508d1|2020-04-19--18-44-15", HONDA.HONDA_HRV),
  CarTestRoute("320098ff6c5e4730|2023-04-13--17-47-46", HONDA.HONDA_HRV_3G),
  CarTestRoute("147613502316e718/00000001--dd141a3140", HONDA.HONDA_HRV_3G),  # Brazilian model
  CarTestRoute("917b074700869333|2021-05-24--20-40-20", HONDA.ACURA_ILX),
  CarTestRoute("08a3deb07573f157|2020-03-06--16-11-19", HONDA.HONDA_ACCORD),  # 1.5T
  CarTestRoute("1da5847ac2488106|2021-05-24--19-31-50", HONDA.HONDA_ACCORD),  # 2.0T
  CarTestRoute("085ac1d942c35910|2021-03-25--20-11-15", HONDA.HONDA_ACCORD),  # 2021 with new style HUD msgs
  CarTestRoute("07585b0da3c88459|2021-05-26--18-52-04", HONDA.HONDA_ACCORD),  # hybrid
  CarTestRoute("f29e2b57a55e7ad5|2021-03-24--20-52-38", HONDA.HONDA_ACCORD),  # hybrid, 2021 with new style HUD msgs
  CarTestRoute("1ad763dd22ef1a0e|2020-02-29--18-37-03", HONDA.HONDA_CRV_5G),
  CarTestRoute("0a96f86fcfe35964|2020-02-05--07-25-51", HONDA.HONDA_ODYSSEY),
  CarTestRoute("d83f36766f8012a5|2020-02-05--18-42-21", HONDA.HONDA_CIVIC_BOSCH_DIESEL),
  CarTestRoute("f0890d16a07a236b|2021-05-25--17-27-22", HONDA.HONDA_INSIGHT),
  CarTestRoute("07d37d27996096b6|2020-03-04--21-57-27", HONDA.HONDA_PILOT),
  CarTestRoute("684e8f96bd491a0e|2021-11-03--11-08-42", HONDA.HONDA_PILOT),  # Passport
  CarTestRoute("0a78dfbacc8504ef|2020-03-04--13-29-55", HONDA.HONDA_CIVIC_BOSCH),
  CarTestRoute("f34a60d68d83b1e5|2020-10-06--14-35-55", HONDA.ACURA_RDX),
  CarTestRoute("54fd8451b3974762|2021-04-01--14-50-10", HONDA.HONDA_RIDGELINE),
  CarTestRoute("2d5808fae0b38ac6|2021-09-01--17-14-11", HONDA.HONDA_E),
  CarTestRoute("f44aa96ace22f34a|2021-12-22--06-22-31", HONDA.HONDA_CIVIC_2022),

  CarTestRoute("87d7f06ade479c2e|2023-09-11--23-30-11", HYUNDAI.HYUNDAI_AZERA_6TH_GEN),
  CarTestRoute("66189dd8ec7b50e6|2023-09-20--07-02-12", HYUNDAI.HYUNDAI_AZERA_HEV_6TH_GEN),
  CarTestRoute("6fe86b4e410e4c37|2020-07-22--16-27-13", HYUNDAI.HYUNDAI_GENESIS),
  CarTestRoute("b5d6dc830ad63071|2022-12-12--21-28-25", HYUNDAI.GENESIS_GV60_EV_1ST_GEN, segment=12),
  CarTestRoute("70c5bec28ec8e345|2020-08-08--12-22-23", HYUNDAI.GENESIS_G70),
  CarTestRoute("ca4de5b12321bd98|2022-10-18--21-15-59", HYUNDAI.GENESIS_GV70_1ST_GEN),
  CarTestRoute("afe09b9f5d3f3548/00000011--15fefe1c50", HYUNDAI.GENESIS_GV70_ELECTRIFIED_1ST_GEN),
  CarTestRoute("afe09b9f5d3f3548/0000001b--a1129a4a15", HYUNDAI.GENESIS_GV70_ELECTRIFIED_1ST_GEN),  # openpilot longitudinal enabled
  CarTestRoute("6b301bf83f10aa90|2020-11-22--16-45-07", HYUNDAI.GENESIS_G80),
  CarTestRoute("66eaa6c3b6b2afc6/00000009--3a5199aabe", HYUNDAI.GENESIS_G80_2ND_GEN_FL),  # HDA2
  CarTestRoute("0bbe367c98fa1538|2023-09-16--00-16-49", HYUNDAI.HYUNDAI_CUSTIN_1ST_GEN),
  CarTestRoute("f0709d2bc6ca451f|2022-10-15--08-13-54", HYUNDAI.HYUNDAI_SANTA_CRUZ_1ST_GEN),
  CarTestRoute("4dbd55df87507948|2022-03-01--09-45-38", HYUNDAI.HYUNDAI_SANTA_FE),
  CarTestRoute("bf43d9df2b660eb0|2021-09-23--14-16-37", HYUNDAI.HYUNDAI_SANTA_FE_2022),
  CarTestRoute("37398f32561a23ad|2021-11-18--00-11-35", HYUNDAI.HYUNDAI_SANTA_FE_HEV_2022),
  CarTestRoute("656ac0d830792fcc|2021-12-28--14-45-56", HYUNDAI.HYUNDAI_SANTA_FE_PHEV_2022, segment=1),
  CarTestRoute("de59124955b921d8|2023-06-24--00-12-50", HYUNDAI.KIA_CARNIVAL_4TH_GEN),
  CarTestRoute("409c9409979a8abc|2023-07-11--09-06-44", HYUNDAI.KIA_CARNIVAL_4TH_GEN),  # Chinese model
  CarTestRoute("e0e98335f3ebc58f|2021-03-07--16-38-29", HYUNDAI.KIA_CEED),
  CarTestRoute("7653b2bce7bcfdaa|2020-03-04--15-34-32", HYUNDAI.KIA_OPTIMA_G4),
  CarTestRoute("018654717bc93d7d|2022-09-19--23-11-10", HYUNDAI.KIA_OPTIMA_G4_FL, segment=0),
  CarTestRoute("f9716670b2481438|2023-08-23--14-49-50", HYUNDAI.KIA_OPTIMA_H),
  CarTestRoute("6a42c1197b2a8179|2023-09-21--10-23-44", HYUNDAI.KIA_OPTIMA_H_G4_FL),
  CarTestRoute("c75a59efa0ecd502|2021-03-11--20-52-55", HYUNDAI.KIA_SELTOS),
  CarTestRoute("5b7c365c50084530|2020-04-15--16-13-24", HYUNDAI.HYUNDAI_SONATA),
  CarTestRoute("b2a38c712dcf90bd|2020-05-18--18-12-48", HYUNDAI.HYUNDAI_SONATA_LF),
  CarTestRoute("c344fd2492c7a9d2|2023-12-11--09-03-23", HYUNDAI.HYUNDAI_STARIA_4TH_GEN),
  CarTestRoute("fb3fd42f0baaa2f8|2022-03-30--15-25-05", HYUNDAI.HYUNDAI_TUCSON),
  CarTestRoute("db68bbe12250812c|2022-12-05--00-54-12", HYUNDAI.HYUNDAI_TUCSON_4TH_GEN),  # 2023
  CarTestRoute("36e10531feea61a4|2022-07-25--13-37-42", HYUNDAI.HYUNDAI_TUCSON_4TH_GEN),  # hybrid
  CarTestRoute("5875672fc1d4bf57|2020-07-23--21-33-28", HYUNDAI.KIA_SORENTO),
  CarTestRoute("1d0d000db3370fd0|2023-01-04--22-28-42", HYUNDAI.KIA_SORENTO_4TH_GEN, segment=5),
  CarTestRoute("fc19648042eb6896|2023-08-16--11-43-27", HYUNDAI.KIA_SORENTO_HEV_4TH_GEN, segment=14),
  CarTestRoute("628935d7d3e5f4f7|2022-11-30--01-12-46", HYUNDAI.KIA_SORENTO_HEV_4TH_GEN),  # plug-in hybrid
  CarTestRoute("9c917ba0d42ffe78|2020-04-17--12-43-19", HYUNDAI.HYUNDAI_PALISADE),
  CarTestRoute("05a8f0197fdac372|2022-10-19--14-14-09", HYUNDAI.HYUNDAI_IONIQ_5),  # HDA2
  CarTestRoute("eb4eae1476647463|2023-08-26--18-07-04", HYUNDAI.HYUNDAI_IONIQ_6, segment=6),  # HDA2
  CarTestRoute("3f29334d6134fcd4|2022-03-30--22-00-50", HYUNDAI.HYUNDAI_IONIQ_PHEV_2019),
  CarTestRoute("fa8db5869167f821|2021-06-10--22-50-10", HYUNDAI.HYUNDAI_IONIQ_PHEV),
  CarTestRoute("e1107f9d04dfb1e2|2023-09-05--22-32-12", HYUNDAI.HYUNDAI_IONIQ_PHEV),  # openpilot longitudinal enabled
  CarTestRoute("2c5cf2dd6102e5da|2020-12-17--16-06-44", HYUNDAI.HYUNDAI_IONIQ_EV_2020),
  CarTestRoute("610ebb9faaad6b43|2020-06-13--15-28-36", HYUNDAI.HYUNDAI_IONIQ_EV_LTD),
  CarTestRoute("2c5cf2dd6102e5da|2020-06-26--16-00-08", HYUNDAI.HYUNDAI_IONIQ),
  CarTestRoute("012c95f06918eca4|2023-01-15--11-19-36", HYUNDAI.HYUNDAI_IONIQ),  # openpilot longitudinal enabled
  CarTestRoute("ab59fe909f626921|2021-10-18--18-34-28", HYUNDAI.HYUNDAI_IONIQ_HEV_2022),
  CarTestRoute("22d955b2cd499c22|2020-08-10--19-58-21", HYUNDAI.HYUNDAI_KONA),
  CarTestRoute("efc48acf44b1e64d|2021-05-28--21-05-04", HYUNDAI.HYUNDAI_KONA_EV),
  CarTestRoute("f90d3cd06caeb6fa|2023-09-06--17-15-47", HYUNDAI.HYUNDAI_KONA_EV),  # openpilot longitudinal enabled
  CarTestRoute("ff973b941a69366f|2022-07-28--22-01-19", HYUNDAI.HYUNDAI_KONA_EV_2022, segment=11),
  CarTestRoute("1618132d68afc876|2023-08-27--09-32-14", HYUNDAI.HYUNDAI_KONA_EV_2ND_GEN, segment=13),
  CarTestRoute("49f3c13141b6bc87|2021-07-28--08-05-13", HYUNDAI.HYUNDAI_KONA_HEV),
  CarTestRoute("a74afe0cf708748f|2023-09-10--11-18-49", HYUNDAI.HYUNDAI_NEXO_1ST_GEN),
  CarTestRoute("5dddcbca6eb66c62|2020-07-26--13-24-19", HYUNDAI.KIA_STINGER),
  CarTestRoute("5b50b883a4259afb|2022-11-09--15-00-42", HYUNDAI.KIA_STINGER_2022),
  CarTestRoute("d624b3d19adce635|2020-08-01--14-59-12", HYUNDAI.HYUNDAI_VELOSTER),
  CarTestRoute("d545129f3ca90f28|2022-10-19--09-22-54", HYUNDAI.KIA_EV6),  # HDA2
  CarTestRoute("68d6a96e703c00c9|2022-09-10--16-09-39", HYUNDAI.KIA_EV6),  # HDA1
  CarTestRoute("9b25e8c1484a1b67|2023-04-13--10-41-45", HYUNDAI.KIA_EV6),
  CarTestRoute("007d5e4ad9f86d13|2021-09-30--15-09-23", HYUNDAI.KIA_K5_2021),
  CarTestRoute("c58dfc9fc16590e0|2023-01-14--13-51-48", HYUNDAI.KIA_K5_HEV_2020),
  CarTestRoute("78ad5150de133637|2023-09-13--16-15-57", HYUNDAI.KIA_K8_HEV_1ST_GEN),
  CarTestRoute("50c6c9b85fd1ff03|2020-10-26--17-56-06", HYUNDAI.KIA_NIRO_EV),
  CarTestRoute("b153671049a867b3|2023-04-05--10-00-30", HYUNDAI.KIA_NIRO_EV_2ND_GEN),
  CarTestRoute("173219cf50acdd7b|2021-07-05--10-27-41", HYUNDAI.KIA_NIRO_PHEV),
  CarTestRoute("23349923ba5c4e3b|2023-12-02--08-51-54", HYUNDAI.KIA_NIRO_PHEV_2022),
  CarTestRoute("34a875f29f69841a|2021-07-29--13-02-09", HYUNDAI.KIA_NIRO_HEV_2021),
  CarTestRoute("db04d2c63990e3ba|2023-02-08--16-52-39", HYUNDAI.KIA_NIRO_HEV_2ND_GEN),
  CarTestRoute("50a2212c41f65c7b|2021-05-24--16-22-06", HYUNDAI.KIA_FORTE),
  CarTestRoute("192283cdbb7a58c2|2022-10-15--01-43-18", HYUNDAI.KIA_SPORTAGE_5TH_GEN),
  CarTestRoute("09559f1fcaed4704|2023-11-16--02-24-57", HYUNDAI.KIA_SPORTAGE_5TH_GEN),  # openpilot longitudinal
  CarTestRoute("b3537035ffe6a7d6|2022-10-17--15-23-49", HYUNDAI.KIA_SPORTAGE_5TH_GEN),  # hybrid
  CarTestRoute("c5ac319aa9583f83|2021-06-01--18-18-31", HYUNDAI.HYUNDAI_ELANTRA),
  CarTestRoute("734ef96182ddf940|2022-10-02--16-41-44", HYUNDAI.HYUNDAI_ELANTRA_GT_I30),
  CarTestRoute("82e9cdd3f43bf83e|2021-05-15--02-42-51", HYUNDAI.HYUNDAI_ELANTRA_2021),
  CarTestRoute("715ac05b594e9c59|2021-06-20--16-21-07", HYUNDAI.HYUNDAI_ELANTRA_HEV_2021),
  CarTestRoute("7120aa90bbc3add7|2021-08-02--07-12-31", HYUNDAI.HYUNDAI_SONATA_HYBRID),
  CarTestRoute("715ac05b594e9c59|2021-10-27--23-24-56", HYUNDAI.GENESIS_G70_2020),
  CarTestRoute("6b0d44d22df18134|2023-05-06--10-36-55", HYUNDAI.GENESIS_GV80),

  CarTestRoute("00c829b1b7613dea|2021-06-24--09-10-10", TOYOTA.TOYOTA_ALPHARD_TSS2),
  CarTestRoute("912119ebd02c7a42|2022-03-19--07-24-50", TOYOTA.TOYOTA_ALPHARD_TSS2),  # hybrid
  CarTestRoute("000cf3730200c71c|2021-05-24--10-42-05", TOYOTA.TOYOTA_AVALON),
  CarTestRoute("0bb588106852abb7|2021-05-26--12-22-01", TOYOTA.TOYOTA_AVALON_2019),
  CarTestRoute("87bef2930af86592|2021-05-30--09-40-54", TOYOTA.TOYOTA_AVALON_2019),  # hybrid
  CarTestRoute("e9966711cfb04ce3|2022-01-11--07-59-43", TOYOTA.TOYOTA_AVALON_TSS2),
  CarTestRoute("eca1080a91720a54|2022-03-17--13-32-29", TOYOTA.TOYOTA_AVALON_TSS2),  # hybrid
  CarTestRoute("6cdecc4728d4af37|2020-02-23--15-44-18", TOYOTA.TOYOTA_CAMRY),
  CarTestRoute("2f37c007683e85ba|2023-09-02--14-39-44", TOYOTA.TOYOTA_CAMRY),  # openpilot longitudinal, with radar CAN filter
  CarTestRoute("54034823d30962f5|2021-05-24--06-37-34", TOYOTA.TOYOTA_CAMRY),  # hybrid
  CarTestRoute("3456ad0cd7281b24|2020-12-13--17-45-56", TOYOTA.TOYOTA_CAMRY_TSS2),
  CarTestRoute("ffccc77938ddbc44|2021-01-04--16-55-41", TOYOTA.TOYOTA_CAMRY_TSS2),  # hybrid
  CarTestRoute("4e45c89c38e8ec4d|2021-05-02--02-49-28", TOYOTA.TOYOTA_COROLLA),
  CarTestRoute("5f5afb36036506e4|2019-05-14--02-09-54", TOYOTA.TOYOTA_COROLLA_TSS2),
  CarTestRoute("5ceff72287a5c86c|2019-10-19--10-59-02", TOYOTA.TOYOTA_COROLLA_TSS2),  # hybrid
  CarTestRoute("d2525c22173da58b|2021-04-25--16-47-04", TOYOTA.TOYOTA_PRIUS),
  CarTestRoute("b14c5b4742e6fc85|2020-07-28--19-50-11", TOYOTA.TOYOTA_RAV4),
  CarTestRoute("32a7df20486b0f70|2020-02-06--16-06-50", TOYOTA.TOYOTA_RAV4H),
  CarTestRoute("cdf2f7de565d40ae|2019-04-25--03-53-41", TOYOTA.TOYOTA_RAV4_TSS2),
  CarTestRoute("a5c341bb250ca2f0|2022-05-18--16-05-17", TOYOTA.TOYOTA_RAV4_TSS2_2022),
  CarTestRoute("ad5a3fa719bc2f83|2023-10-17--19-48-42", TOYOTA.TOYOTA_RAV4_TSS2_2023),
  CarTestRoute("7e34a988419b5307|2019-12-18--19-13-30", TOYOTA.TOYOTA_RAV4_TSS2),  # hybrid
  CarTestRoute("2475fb3eb2ffcc2e|2022-04-29--12-46-23", TOYOTA.TOYOTA_RAV4_TSS2_2022),  # hybrid
  CarTestRoute("7a31f030957b9c85|2023-04-01--14-12-51", TOYOTA.LEXUS_ES),
  CarTestRoute("37041c500fd30100|2020-12-30--12-17-24", TOYOTA.LEXUS_ES),  # hybrid
  CarTestRoute("e6a24be49a6cd46e|2019-10-29--10-52-42", TOYOTA.LEXUS_ES_TSS2),
  CarTestRoute("f49e8041283f2939|2019-05-30--11-51-51", TOYOTA.LEXUS_ES_TSS2),  # hybrid
  CarTestRoute("da23c367491f53e2|2021-05-21--09-09-11", TOYOTA.LEXUS_CTH, segment=3),
  CarTestRoute("32696cea52831b02|2021-11-19--18-13-30", TOYOTA.LEXUS_RC),
  CarTestRoute("ab9b64a5e5960cba|2023-10-24--17-32-08", TOYOTA.LEXUS_GS_F),
  CarTestRoute("886fcd8408d570e9|2020-01-29--02-18-55", TOYOTA.LEXUS_RX),
  CarTestRoute("d27ad752e9b08d4f|2021-05-26--19-39-51", TOYOTA.LEXUS_RX),  # hybrid
  CarTestRoute("01b22eb2ed121565|2020-02-02--11-25-51", TOYOTA.LEXUS_RX_TSS2),
  CarTestRoute("b74758c690a49668|2020-05-20--15-58-57", TOYOTA.LEXUS_RX_TSS2),  # hybrid
  CarTestRoute("964c09eb11ca8089|2020-11-03--22-04-00", TOYOTA.LEXUS_NX),
  CarTestRoute("ec429c0f37564e3c|2020-02-01--17-28-12", TOYOTA.LEXUS_NX),  # hybrid
  CarTestRoute("3fd5305f8b6ca765|2021-04-28--19-26-49", TOYOTA.LEXUS_NX_TSS2),
  CarTestRoute("09ae96064ed85a14|2022-06-09--12-22-31", TOYOTA.LEXUS_NX_TSS2),  # hybrid
  CarTestRoute("4765fbbf59e3cd88|2024-02-06--17-45-32", TOYOTA.LEXUS_LC_TSS2),
  CarTestRoute("0a302ffddbb3e3d3|2020-02-08--16-19-08", TOYOTA.TOYOTA_HIGHLANDER_TSS2),
  CarTestRoute("437e4d2402abf524|2021-05-25--07-58-50", TOYOTA.TOYOTA_HIGHLANDER_TSS2),  # hybrid
  CarTestRoute("3183cd9b021e89ce|2021-05-25--10-34-44", TOYOTA.TOYOTA_HIGHLANDER),
  CarTestRoute("80d16a262e33d57f|2021-05-23--20-01-43", TOYOTA.TOYOTA_HIGHLANDER),  # hybrid
  CarTestRoute("eb6acd681135480d|2019-06-20--20-00-00", TOYOTA.TOYOTA_SIENNA),
  CarTestRoute("2e07163a1ba9a780|2019-08-25--13-15-13", TOYOTA.LEXUS_IS),
  CarTestRoute("649bf2997ada6e3a|2023-08-08--18-04-22", TOYOTA.LEXUS_IS_TSS2),
  CarTestRoute("0a0de17a1e6a2d15|2020-09-21--21-24-41", TOYOTA.TOYOTA_PRIUS_TSS2),
  CarTestRoute("9b36accae406390e|2021-03-30--10-41-38", TOYOTA.TOYOTA_MIRAI),
  CarTestRoute("cd9cff4b0b26c435|2021-05-13--15-12-39", TOYOTA.TOYOTA_CHR),
  CarTestRoute("57858ede0369a261|2021-05-18--20-34-20", TOYOTA.TOYOTA_CHR),  # hybrid
  CarTestRoute("ea8fbe72b96a185c|2023-02-08--15-11-46", TOYOTA.TOYOTA_CHR_TSS2),
  CarTestRoute("6719965b0e1d1737|2023-02-09--22-44-05", TOYOTA.TOYOTA_CHR_TSS2),  # hybrid
  CarTestRoute("6719965b0e1d1737|2023-08-29--06-40-05", TOYOTA.TOYOTA_CHR_TSS2),  # hybrid, openpilot longitudinal, radar disabled
  CarTestRoute("14623aae37e549f3|2021-10-24--01-20-49", TOYOTA.TOYOTA_PRIUS_V),

  CarTestRoute("202c40641158a6e5|2021-09-21--09-43-24", VOLKSWAGEN.VOLKSWAGEN_ARTEON_MK1),
  CarTestRoute("2c68dda277d887ac|2021-05-11--15-22-20", VOLKSWAGEN.VOLKSWAGEN_ATLAS_MK1),
  CarTestRoute("ffcd23abbbd02219|2024-02-28--14-59-38", VOLKSWAGEN.VOLKSWAGEN_CADDY_MK3),
  CarTestRoute("cae14e88932eb364|2021-03-26--14-43-28", VOLKSWAGEN.VOLKSWAGEN_GOLF_MK7),  # Stock ACC
  CarTestRoute("3cfdec54aa035f3f|2022-10-13--14-58-58", VOLKSWAGEN.VOLKSWAGEN_GOLF_MK7),  # openpilot longitudinal
  CarTestRoute("578742b26807f756|00000010--41ee3e5bec", VOLKSWAGEN.VOLKSWAGEN_JETTA_MK6),
  CarTestRoute("58a7d3b707987d65|2021-03-25--17-26-37", VOLKSWAGEN.VOLKSWAGEN_JETTA_MK7),
  CarTestRoute("4d134e099430fba2|2021-03-26--00-26-06", VOLKSWAGEN.VOLKSWAGEN_PASSAT_MK8),
  CarTestRoute("3cfdec54aa035f3f|2022-07-19--23-45-10", VOLKSWAGEN.VOLKSWAGEN_PASSAT_NMS),
  CarTestRoute("0cd0b7f7e31a3853|2021-11-03--19-30-22", VOLKSWAGEN.VOLKSWAGEN_POLO_MK6),
  CarTestRoute("064d1816e448f8eb|2022-09-29--15-32-34", VOLKSWAGEN.VOLKSWAGEN_SHARAN_MK2),
  CarTestRoute("7d82b2f3a9115f1f|2021-10-21--15-39-42", VOLKSWAGEN.VOLKSWAGEN_TAOS_MK1),
  CarTestRoute("2744c89a8dda9a51|2021-07-24--21-28-06", VOLKSWAGEN.VOLKSWAGEN_TCROSS_MK1),
  CarTestRoute("2cef8a0b898f331a|2021-03-25--20-13-57", VOLKSWAGEN.VOLKSWAGEN_TIGUAN_MK2),
  CarTestRoute("a589dcc642fdb10a|2021-06-14--20-54-26", VOLKSWAGEN.VOLKSWAGEN_TOURAN_MK2),
  CarTestRoute("a459f4556782eba1|2021-09-19--09-48-00", VOLKSWAGEN.VOLKSWAGEN_TRANSPORTER_T61),
  CarTestRoute("0cd0b7f7e31a3853|2021-11-18--00-38-32", VOLKSWAGEN.VOLKSWAGEN_TROC_MK1),
  CarTestRoute("07667b885add75fd|2021-01-23--19-48-42", VOLKSWAGEN.AUDI_A3_MK3),
  CarTestRoute("6c6b466346192818|2021-06-06--14-17-47", VOLKSWAGEN.AUDI_Q2_MK1),
  CarTestRoute("0cd0b7f7e31a3853|2021-12-03--03-12-05", VOLKSWAGEN.AUDI_Q3_MK2),
  CarTestRoute("8f205bdd11bcbb65|2021-03-26--01-00-17", VOLKSWAGEN.SEAT_ATECA_MK1),
  CarTestRoute("fc6b6c9a3471c846|2021-05-27--13-39-56", VOLKSWAGEN.SEAT_ATECA_MK1),  # Leon
  CarTestRoute("0bbe367c98fa1538|2023-03-04--17-46-11", VOLKSWAGEN.SKODA_FABIA_MK4),
  CarTestRoute("12d6ae3057c04b0d|2021-09-15--00-04-07", VOLKSWAGEN.SKODA_KAMIQ_MK1),
  CarTestRoute("12d6ae3057c04b0d|2021-09-04--21-21-21", VOLKSWAGEN.SKODA_KAROQ_MK1),
  CarTestRoute("90434ff5d7c8d603|2021-03-15--12-07-31", VOLKSWAGEN.SKODA_KODIAQ_MK1),
  CarTestRoute("66e5edc3a16459c5|2021-05-25--19-00-29", VOLKSWAGEN.SKODA_OCTAVIA_MK3),
  CarTestRoute("026b6d18fba6417f|2021-03-26--09-17-04", VOLKSWAGEN.SKODA_KAMIQ_MK1),  # Scala
  CarTestRoute("b2e9858e29db492b|2021-03-26--16-58-42", VOLKSWAGEN.SKODA_SUPERB_MK3),

  CarTestRoute("3c8f0c502e119c1c|2020-06-30--12-58-02", SUBARU.SUBARU_ASCENT),
  CarTestRoute("c321c6b697c5a5ff|2020-06-23--11-04-33", SUBARU.SUBARU_FORESTER),
  CarTestRoute("791340bc01ed993d|2019-03-10--16-28-08", SUBARU.SUBARU_IMPREZA),
  CarTestRoute("8bf7e79a3ce64055|2021-05-24--09-36-27", SUBARU.SUBARU_IMPREZA_2020),
  CarTestRoute("8de015561e1ea4a0|2023-08-29--17-08-31", SUBARU.SUBARU_IMPREZA),  # openpilot longitudinal
  # CarTestRoute("c3d1ccb52f5f9d65|2023-07-22--01-23-20", SUBARU.OUTBACK, segment=9), # gen2 longitudinal, eyesight disabled
  CarTestRoute("1bbe6bf2d62f58a8|2022-07-14--17-11-43", SUBARU.SUBARU_OUTBACK, segment=10),
  CarTestRoute("c56e69bbc74b8fad|2022-08-18--09-43-51", SUBARU.SUBARU_LEGACY, segment=3),
  CarTestRoute("f4e3a0c511a076f4|2022-08-04--16-16-48", SUBARU.SUBARU_CROSSTREK_HYBRID, segment=2),
  CarTestRoute("7fd1e4f3a33c1673|2022-12-04--15-09-53", SUBARU.SUBARU_FORESTER_2022, segment=4),
  CarTestRoute("f3b34c0d2632aa83|2023-07-23--20-43-25", SUBARU.SUBARU_OUTBACK_2023, segment=7),
  CarTestRoute("99437cef6d5ff2ee|2023-03-13--21-21-38", SUBARU.SUBARU_ASCENT_2023, segment=7),
  # Pre-global, dashcam
  CarTestRoute("95441c38ae8c130e|2020-06-08--12-10-17", SUBARU.SUBARU_FORESTER_PREGLOBAL),
  CarTestRoute("df5ca7660000fba8|2020-06-16--17-37-19", SUBARU.SUBARU_LEGACY_PREGLOBAL),
  CarTestRoute("5ab784f361e19b78|2020-06-08--16-30-41", SUBARU.SUBARU_OUTBACK_PREGLOBAL),
  CarTestRoute("e19eb5d5353b1ac1|2020-08-09--14-37-56", SUBARU.SUBARU_OUTBACK_PREGLOBAL_2018),

  CarTestRoute("fbbfa6af821552b9|2020-03-03--08-09-43", NISSAN.NISSAN_XTRAIL),
  CarTestRoute("5b7c365c50084530|2020-03-25--22-10-13", NISSAN.NISSAN_LEAF),
  CarTestRoute("22c3dcce2dd627eb|2020-12-30--16-38-48", NISSAN.NISSAN_LEAF_IC),
  CarTestRoute("059ab9162e23198e|2020-05-30--09-41-01", NISSAN.NISSAN_ROGUE),
  CarTestRoute("b72d3ec617c0a90f|2020-12-11--15-38-17", NISSAN.NISSAN_ALTIMA),

  CarTestRoute("32a319f057902bb3|2020-04-27--15-18-58", MAZDA.MAZDA_CX5),
  CarTestRoute("10b5a4b380434151|2020-08-26--17-11-45", MAZDA.MAZDA_CX9),
  CarTestRoute("74f1038827005090|2020-08-26--20-05-50", MAZDA.MAZDA_3),
  CarTestRoute("fb53c640f499b73d|2021-06-01--04-17-56", MAZDA.MAZDA_6),
  CarTestRoute("f6d5b1a9d7a1c92e|2021-07-08--06-56-59", MAZDA.MAZDA_CX9_2021),
  CarTestRoute("a4af1602d8e668ac|2022-02-03--12-17-07", MAZDA.MAZDA_CX5_2022),

  # Segments that test specific issues
  # Controls mismatch due to standstill threshold
  CarTestRoute("bec2dcfde6a64235|2022-04-08--14-21-32", HONDA.HONDA_CRV_HYBRID, segment=22),
]
