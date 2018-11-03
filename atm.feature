 # Cash transactions via ATM
 # Money in ATM must cover the cash withdrawal amount.
 # Account balance must cover the cash and fee.
 # Gold account: Maximum cash withdrawal 700 EUR. Cash withdrawal fee is 1 EUR + 0.5% of the amount.
 # Platinum account: Maximum cash withdrawal 2000 EUR. Cash withdrawal fee is 1 EUR.
 # Cash deposit: 0.5% of the amount for Gold account, free for Platinum account.
  Feature: ATM cash withdrawal. Functional testing.
  
  Scenario Outline: Simple Platinum withdraw from ATM with more than 2000 EUR
    Given I have a Platinum account and am withdrawing cash from an ATM
    When I have "<a>" on my account and want to withdraw "<w>"
    Then the ATM returns "<sum>"

    Examples:
        |  a  |  w | sum |
        |  -1  |  1 |  0  |
        |  0  |  1 |  0  |
        |  1  |  1 |  0  |
        |  2  |  -1 |  0  |
        |  2  |  1 |  1  |
        |  200  | 100  |  100  |
        |  2011  |  1999 |  1999  |
        |  2011  |  2000 |  2000  |
        |  5000  |  2001 |  0  |
		
  
