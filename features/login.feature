Feature: OrangeHRM Login

  Scenario: Successful login with valid credentials
    Given the user is on the OrangeHRM login page
    When the user enters the valid username and password
    And clicks the login button
    Then the user should see the dashboard
