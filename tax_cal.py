import math


def cal_income_tax_percentage(income_amount):
    # 195万以下の場合
    if income_amount <= 1950000:
        return {"tax": 0.05, "deduction_amount": 0}
    # 195万超 330万円以下の場合
    if 1950000 <= income_amount <= 3300000:
        return {"tax": 0.1, "deduction_amount": 97500}
    # 330万超 695万円以下の場合
    if 3300000 <= income_amount <= 6950000:
        return {"tax": 0.2, "deduction_amount": 427500}
    # 695万超 900万円以下の場合
    if 6950000 <= income_amount <= 9000000:
        return {"tax": 0.23, "deduction_amount": 636000}
    # 900万超 1800万円以下の場合
    if 9000000 <= income_amount <= 18000000:
        return {"tax": 0.33, "deduction_amount": 1536000}
    # 1800万超 4000万円以下の場合
    if 18000000 <= income_amount <= 40000000:
        return {"tax": 0.4, "deduction_amount": 2796000}
    # 4000万以上の場合
    if income_amount >= 40000000:
        return {"tax": 0.45, "deduction_amount": 4796000}


class Tax:
    def __init__(self):
        # 売り上げ
        self.earnings = int(input("売り上げの合計を入力してください \n"))
        # 必要経費
        self.expenses = int(input("経費の合計を入力してください \n"))
        # 基礎控除
        self.standard_deduction_amount = 480000
        # 役職
        self.tier = input("tierを入力してください")
        # 個人事業税　 ※課税所得が２９０万を超えた場合に発生
        self.personal_business_tax = 1.05
        # 税額控除
        self.tax_credit = 0
        # 住民税税額控除
        self.resident_tax = 1.10
        # 青色申告特別控除
        self.blue_declaration_special_deduction = 550000
        # 復興特別所得税
        self.reconstruction_special_income_tax = 1.021

    def cal_tax(self):
        # 所得金額
        income_amount = self.earnings - self.expenses - self.standard_deduction_amount
        # 課税所得金額 ・ 納税額
        taxable_income_amount = (income_amount - self.blue_declaration_special_deduction - cal_income_tax_percentage(income_amount)["deduction_amount"]) * cal_income_tax_percentage(income_amount)["tax"] * self.reconstruction_special_income_tax
        # 申告納税額
        declared_tax_payment_amount = taxable_income_amount - self.tax_credit
        # 収める税額
        return print("売り上げが" + str(self.earnings) + "円, 経費が" + str(self.expenses) + "円で \n合計" + str(
            math.floor(int(declared_tax_payment_amount) if math.floor(int(declared_tax_payment_amount)) > 0 else 0)) + "円の税金がかかります")


tax = Tax()
tax.cal_tax()
