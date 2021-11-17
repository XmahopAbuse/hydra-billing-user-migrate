from initial_db.hydra_db import HydraDB


class CreatePhone():
    """Привязка телефона к физическому лицу"""

    hydra = HydraDB().connect()

    def __init__(self, person_id, number):
        self.number = number
        self.person_id = person_id

    def create(self):
        try:
            self.hydra.execute(f"""
                DECLARE
                    num_N_ADDRESS_ID                       SI_ADDRESSES.N_ADDRESS_ID%TYPE;
                    num_N_SUBJ_ADDRESS_ID                  SI_SUBJ_ADDRESSES.N_SUBJ_ADDRESS_ID%TYPE;
                BEGIN
                SI_ADDRESSES_PKG.SI_SUBJ_ADDRESSES_PUT_EX(
                              num_N_SUBJ_ADDRESS_ID               => num_N_SUBJ_ADDRESS_ID, --вернет ID связки
                              num_N_ADDRESS_ID                    => num_N_ADDRESS_ID, -- вернет ID адреса
                              num_N_SUBJECT_ID                    => {self.person_id}, -- указать ID СУ
                              vch_VC_CODE                         => '{self.number}', -- сам адрес
                              num_N_SUBJ_ADDR_TYPE_ID             => 12016, --тип для уведомлений
                              num_N_ADDR_TYPE_ID                  => 13006);-- тип телефон;
                  COMMIT;
                END;
            """)
            return {"message": "Доступ в личный кабинет предоставлен"}
        except:
            return {"message": "Не удалось предоставить доступ в личный кабинет"}
