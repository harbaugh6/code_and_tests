// This test file is used to demonstrate basic understanding of both the Playwright tool and Typescript used to construct
// the test fixtures.

import { test, expect } from '@playwright/test';
import { Homepage } from '../fixtures/homepage';
import users from '../.auth/users'

let homepage;
const baseURL = 'http://capalum.org'


test.describe('CAN Homepage tests', () => {

    test.beforeEach(async ({page}) => {
        homepage = new Homepage(page);
    });

    test('should go to the CAN homepage and sign in', async ({page}) => {
        await page.goto(baseURL);
        await expect(page).toHaveTitle(/Capitol Alumni Network/);
        await homepage.signIn();
        await page.getByPlaceholder('Email address').click();
        await page.getByPlaceholder('Email address').fill(users.canAccount.username);
        await page.getByPlaceholder('Password').fill(users.canAccount.password);
        await page.getByRole('button', { name: 'Sign in with LeagueApps' }).click();
        await expect(page.getByText('Welcome back, Kyle')).toBeVisible();
    })
})