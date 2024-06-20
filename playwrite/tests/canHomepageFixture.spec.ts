import { test as base, expect } from '@playwright/test';
import { Homepage } from '../fixtures/homepage';

// Extend basic test by providing a Homepage fixture.
const test = base.extend<{ homepage: Homepage }>({
    homepage: async ({page}, use) => {
        const homepage = new Homepage(page);
        await page.goto('/');
        await expect(page).toHaveTitle(/Capitol Alumni Network/);
        await use(homepage);
    },
});

// test.beforeEach(async ({page }) => {
//     await page.goto('/');
// })

// Test goes to the CAN login page and will log in with valid credentials
test('should log into the CAN site', async ({page, homepage}) => {
    await homepage.signIn();
    await page.getByPlaceholder('Email address').click();
    await page.getByPlaceholder('Email address').fill("email string");
    await page.getByPlaceholder('Password').fill("password string");
    await page.getByRole('button', { name: 'Sign in with LeagueApps' }).click();
})

// Test goes to the Softball page to validate that Standings are displayed.
test('should go to the Softball page', async ({page, homepage}) => {
    await homepage.goToSoftball();
    await page.getByRole('link', { name: 'Teams, Schedule and Standings' }).click();
    await page.getByRole('link', { name: 'Standings' }).click();
})