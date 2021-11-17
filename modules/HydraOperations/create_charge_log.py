from initial_db.hydra_db import HydraDB
from datetime import datetime
from dateutil.relativedelta import relativedelta


class CreateChargeLog():
    """Выставление акта начисления"""

    hydra = HydraDB().connect()

    def __init__(self, account_id):
        self.account_id = account_id
        self.begin_date = datetime.strftime(datetime.today(),"%d.%m.%Y")
        self.end_date = datetime.strftime(datetime.today() + relativedelta(months=+1), "%d.%m.%Y")


    def create(self):
        try:
            self.hydra.execute(f"""    
                BEGIN
                  -- Выставление инвойсов за определенный период
                  SD_CHARGE_LOGS_CHARGING_PKG.PROCESS_ACCOUNT(
                  num_N_ACCOUNT_ID     => {self.account_id}, -- идентификатор лицевого счета
                  dt_D_OPER            => TO_DATE('{self.begin_date}','DD.MM.YYYY'),  --дата начала
                END;
            """)
            return {"message": "Акт начисления выставлен"}
        except:
            return {"message": "Не удалось выставить акт начисления"}
