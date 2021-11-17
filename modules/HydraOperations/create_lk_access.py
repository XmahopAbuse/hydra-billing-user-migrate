from initial_db.hydra_db import HydraDB

class CreateLKAccess():

    """Доступ к приложению Личный кабинет"""


    hydra = HydraDB().connect()

    def __init__(self, customer_id, login, password):
        self.customer_id = customer_id
        self.login = login
        self.password = password

    def create(self):
        try:
            self.hydra.execute(f"""
                DECLARE
                    num_N_SUBJ_SERV_ID      SI_V_SUBJ_SERVICES.N_SUBJ_SERV_ID % TYPE;
                BEGIN
                    SI_SUBJECTS_PKG.SI_SUBJ_SERVICES_PUT(
                        num_N_SUBJ_SERV_ID => num_N_SUBJ_SERV_ID,
                        num_N_SUBJECT_ID => {self.customer_id},
                        num_N_AUTH_TYPE_ID => SS_CONSTANTS_PKG_S.AUTH_TYPE_LoginPass,
                        num_N_SERVICE_ID => SS_CONSTANTS_PKG_S.NETSERV_ARM_Private_Office,
                        vch_VC_LOGIN => '{self.login}',
                        num_N_SUBJ_SERV_TYPE_ID => SS_CONSTANTS_PKG_S.SUBJ_SERV_AppAccess);
                
                -- Установка пароля
    
                        SI_SUBJECTS_PKG.SI_SUBJ_SERVICES_CHG_PASS(
                        num_N_SUBJ_SERV_ID => num_N_SUBJ_SERV_ID,
                        vch_VC_NEW_PASS => '{self.password}');
                    COMMIT;
                END;
            """)
            return {"message": "Доступ в личный кабинет предоставлен"}
        except:
            return {"message": "Не удалось предоставить доступ в личный кабинет"}
