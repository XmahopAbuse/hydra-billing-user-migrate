from initial_db.hydra_db import HydraDB
import datetime


class InitialBalance():

    """Инициализация баланса на созданном аккаунте"""

    TODAY = datetime.date.today().strftime("%d.%m.%y")

    hydra = HydraDB().connect()

    def __init__(self):
        print(self.TODAY)

    def add_balance(self, sum, customer_id, account_id):

        if int(sum) < 0:
            self.minus_balance(sum, customer_id, account_id)
        else:
            self.plus_balance(sum, customer_id, account_id)


    def plus_balance(self, sum, customer_id, account_id):
        self.hydra.execute(f"""
        DECLARE
            num_N_DOC_ID                   SD_V_DOCUMENTS.N_DOC_ID%TYPE := null;

        BEGIN
            SD_PAYMENTS_PKG.SD_PAYMENTS_CHARGE(
                num_N_DOC_ID,
                num_N_DOC_TYPE_ID       => 5002,
                num_N_REASON_DOC_ID     => null,
                num_N_DOC_STATE_ID      => 4003,
                num_N_PAY_TYPE_ID       => SYS_CONTEXT('CONST', 'VMM_KIND_Virtual'),
                num_N_MOVE_TYPE_ID      => 1007,
                num_N_ACCOUNT_ID_ForWho => {account_id},
                num_N_PAYER_ID          => 100,
                num_N_ACCOUNT_ID_Payer  => 51615001,
                num_N_RECEIVER_ID       => {customer_id},
                num_N_ACCOUNT_ID_Receiver => {account_id},
                dt_D_DOC                => null,
                num_N_SUM               => {sum},
                num_N_TAX_RATE_ID       => 2005,
                num_N_CURRENCY_ID       => 1044,
                b_Virtual               => 1,
                num_N_FIRM_ID           => 100
            );
            commit;
        END;
        """)
    def minus_balance(self, sum, customer_id, account_id):
        self.hydra.execute(f"""
        DECLARE
            num_N_DOC_ID                   SD_V_DOCUMENTS.N_DOC_ID%TYPE := null;

        BEGIN
            SD_PAYMENTS_PKG.SD_PAYMENTS_CHARGE(
                num_N_DOC_ID,
                num_N_DOC_TYPE_ID       => 5002,
                num_N_REASON_DOC_ID     => null,
                num_N_DOC_STATE_ID      => 4003,
                num_N_PAY_TYPE_ID       => SYS_CONTEXT('CONST', 'VMM_KIND_Virtual'),
                num_N_MOVE_TYPE_ID      => 1007,
                num_N_ACCOUNT_ID_ForWho => {account_id},
                num_N_PAYER_ID          => 100,
                num_N_ACCOUNT_ID_Payer  => 51615001,
                num_N_RECEIVER_ID       => {customer_id},
                num_N_ACCOUNT_ID_Receiver => {account_id},
                dt_D_DOC                   => null,
                num_N_SUM               => {sum},
                num_N_TAX_RATE_ID       => 2005,
                num_N_CURRENCY_ID       => 1044,
                b_Virtual               => 1,
                num_N_FIRM_ID           => 100
            );
            commit;
        END;
        """)
