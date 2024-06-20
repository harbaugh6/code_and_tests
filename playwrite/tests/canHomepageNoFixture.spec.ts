import { test, expect } from '@playwright/test';
import { Homepage } from '../fixtures/homepage';

test.describe('CAN Homepage tests', () => {
    let homepage;

    test.beforeEach(async ({page}) => {
        homepage = new Homepage(page);
    });

    test('should go to the CAN homepage and sign in', async ({page}) => {
        await page.goto('/');
        await expect(page).toHaveTitle(/Capitol Alumni Network/);
        await homepage.signIn();
        await page.getByPlaceholder('Email address').click();
        await page.getByPlaceholder('Email address').fill('harbaugh6@gmail.com');
        await page.getByPlaceholder('Password').fill('JessiKyle20!8');
        await page.getByRole('button', { name: 'Sign in with LeagueApps' }).click();
        await expect(page.getByText('Welcome back, Kyle')).toBeVisible();
    })
})