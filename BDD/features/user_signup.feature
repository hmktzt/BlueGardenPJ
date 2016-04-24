Feature: User Signup
  As the System Owner
  I want users to be able to signup for new accounts
  so users can later log in

  Scenario Outline: New user signup
    Given at the signup screen
    When a new user submits <username> <email> and <password>
    Then the system should return "Success" as the signup status of the user
    Examples:
      | username | email | password  |
      | user1     | d@gmail.com | test123   |
      | user2     | a@gmail.com | test123   |

