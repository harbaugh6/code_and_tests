import {test, expect} from '@playwright/test';
import { Homepage } from '../fixtures/homepage';
import {faker} from '@faker-js/faker/locale/en_US';

let homepage;
const baseURL = 'http://capalum.org';
// Creating some test data here in the test itself as an example of what you can do.
// Whether you -should- do it this way is up for debate.
const firstName = faker.person.firstName();
const lastName = (faker.person.lastName() + '+Test1234');
const email = faker.internet.email({firstName, lastName})


test.describe('Can create a new account', () => {
    test.beforeEach(async ({page}) => {
        homepage = new Homepage(page);
    });

    test('should sign up a new user for the CAN website', async ({page}) => {
        await page.goto(baseURL);
        await expect(page).toHaveTitle("Capitol Alumni Network");
        await homepage.signUpLink.click();
        await expect(page).toHaveTitle("LeagueApps Login :: Create Account");
        await expect(page.getByRole("textbox", {name: "First Name"})).toBeVisible();
        await page.getByRole("textbox", {name: "First Name"}).fill(firstName);
        await page.getByRole("textbox", {name: "Last Name"}).fill(lastName);
        await page.getByRole("textbox", {name: "Email Address"}).fill(email);
        // Hardcoding the password for ease of use and to meet the requirements.
        await page.getByRole("textbox", {name: "Password"}).click();
        await page.getByRole("textbox", {name: "Password"}).pressSequentially('Test1234$')
        await page.getByRole("button", {name: "Create a LeagueApps account"}).click();
        await expect(page.getByRole('heading', { name: 'Success!' })).toBeVisible();
    })
})