import {test, expect} from '@playwright/test';
import { Homepage } from '../fixtures/homepage';
import {faker} from '@faker-js/faker/locale/en_US';
import {UserCreator} from '../fixtures/userCreator';

let homepage;
const baseURL = 'http://capalum.org';
// Creating some test data here in the test itself as an example of what you can do.
// Whether you -should- do it this way is up for debate.
const firstName = faker.person.firstName();
const lastName = faker.person.lastName();
const email = faker.internet.email(firstName, lastName + "+Test1234");


test.describe('Can create a new account', () => {
    test.beforeEach(async ({page}) => {
        homepage = new Homepage(page);
    });

    test('should sign up a new user for the CAN website', async ({page}) => {
        await page.goto(baseURL);
        await expect(page).toHaveTitle("Capitol Alumni Network");
        await homepage.signUpLink.click();
        await expect(page).toHaveTitle("LeagueApps Login :: Create Account")
        await page.getByRole("textbox", {name: "First Name"}).fill(firstName);
        await page.getByRole("textbox", {name: "Last Name"}).fill(lastName);
        await page.getByRole("textbox", {name: "Email Address"}).fill(email);
        await page.getByRole("textbox", {name: "Password"}).fill(faker.internet.password())
        // At this point the user would click "Sign Up", however LeagueApps has implemented a
        // pretty stringent anti-automation policy that has thwarted my attempt to complete this test.
    })
})