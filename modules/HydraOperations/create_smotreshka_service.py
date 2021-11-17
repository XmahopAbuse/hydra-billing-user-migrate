from initial_db.hydra_db import HydraDB


class CreateSmotreshkaService():
    """Доступ к приложению Смотрешка"""

    hydra = HydraDB().connect()
    SMOTRESHKA_SERVICE_ID = 51084201

    def __init__(self, customer_id, object_id , user_id):
        self.customer_id = customer_id
        self.object_id = object_id
        self.user_id = user_id
    def create(self):
        try:
            self.hydra.execute(f"""
                    DECLARE
                      num_N_SUBJ_SERV_ID                  SI_V_SUBJ_SERVICES.N_SUBJ_SERV_ID%TYPE;
                    BEGIN
                      -- Добавление записи
                      SI_SUBJECTS_PKG.SI_SUBJ_SERVICES_PUT(
                        num_N_SUBJ_SERV_ID      => num_N_SUBJ_SERV_ID,
                        num_N_SUBJ_SERV_TYPE_ID => SS_CONSTANTS_PKG_S.SUBJ_SERV_ServiceUse,
                        num_N_SUBJECT_ID        => {self.customer_id},
                        num_N_SERVICE_ID        => {self.SMOTRESHKA_SERVICE_ID},
                        num_N_OBJECT_ID         => {self.object_id},
                        num_N_AUTH_TYPE_ID      => SS_CONSTANTS_PKG_S.AUTH_TYPE_LoginPass,
                        vch_VC_VALUE            => 'smotreshka{user_id}@kompel.ru',
                    
                      -- Установка пароля
                      SI_SUBJECTS_PKG.SI_SUBJ_SERVICES_CHG_PASS(
                        num_N_SUBJ_SERV_ID => num_N_SUBJ_SERV_ID,
                        vch_VC_NEW_PASS    => 'uralsky');
                        COMMIT;
                    END;
            """)
            return {"message": "Доступ в личный кабинет предоставлен"}
        except:
            return {"message": "Не удалось предоставить доступ в личный кабинет"}
