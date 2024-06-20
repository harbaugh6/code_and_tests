import { test, expect } from '@playwright/test';
import { before } from 'node:test';


test.describe('Navigation', () => {

  test.beforeAll(async ({page}) => {
    await page.goto('about:blank')
  });

  test('go to CAN website', async ({page}) => {
    await page.goto('/');
    await expect(page).toHaveTitle(/Capitol Alumni Network/);
  });
  
  test('Goes to the softball standing page', async ({ page }) => {  
    await page.goto('/');
    await expect(page.getByRole('link', { name: 'Capitol Alumni Network' })).toBeVisible();
    await page.getByRole('link', { name: '| Sports |' }).hover();
    await page.getByRole('link', { name: 'Softball' }).click();
    await page.getByRole('link', { name: 'Teams, Schedule and Standings' }).click();
    await page.getByRole('link', { name: 'Standings' }).click();
  });
  
  test('Can log into CapAlum with no issues', async ({ page }) => {
    await page.goto('/');
    await page.getByRole('link', { name: 'Sign In' }).click();
    await page.getByPlaceholder('Email address').click();
    await page.getByPlaceholder('Email address').fill('harbaugh6@gmail.com');
    await page.getByPlaceholder('Email address').press('Tab');
    await page.getByPlaceholder('Password').fill('JessiKyle20!8');
    await page.getByRole('button', { name: 'Sign in with LeagueApps' }).click();
    await expect(page.getByText('Welcome back, Kyle')).toBeVisible();
  });
  
  test('cannot log in with invalid credentials', async ({ page }) => {
    await page.goto('/');
    await page.getByRole('link', { name: 'Sign In' }).click();
    await page.getByPlaceholder('Email address').click();
    await page.getByPlaceholder('Email address').fill('harbaugh6@gmail.com');
    await page.getByPlaceholder('Password').click();
    await page.getByPlaceholder('Password').fill('JessiKyle2020');
    await page.getByRole('button', { name: 'Sign in with LeagueApps' }).click();
    await expect(page.getByText('Invalid email or password')).toBeVisible();
  });
});

// test('has title', async ({ page }) => {
//   await page.goto('https://playwright.dev/');

//   // Expect a title "to contain" a substring.
//   await expect(page).toHaveTitle(/Playwright/);
// });

// test('get started link', async ({ page }) => {
//   await page.goto('https://playwright.dev/');

//   // Click the get started link.
//   await page.getByRole('link', { name: 'Get started' }).click();

//   // Expects page to have a heading with the name of Installation.
//   await expect(page.getByRole('heading', { name: 'Installation' })).toBeVisible();
// });

// test('go to CAN website', async ({page}) => {
//   await page.goto('/');

//   await expect(page).toHaveTitle(/Capitol Alumni Network/);
// });

// test('Goes to the softball standing page', async ({ page }) => {  
//   await page.goto('/');
//   await expect(page.getByRole('link', { name: 'Capitol Alumni Network' })).toBeVisible();
//   await page.getByRole('link', { name: '| Sports |' }).hover();
//   await page.getByRole('link', { name: 'Softball' }).click();
//   await page.getByRole('link', { name: 'Teams, Schedule and Standings' }).click();
//   await page.getByRole('link', { name: 'Standings' }).click();
// });

// test('Can log into CapAlum with no issues', async ({ page }) => {
//   await page.goto('/');
//   await page.getByRole('link', { name: 'Sign In' }).click();
//   await page.getByPlaceholder('Email address').click();
//   await page.getByPlaceholder('Email address').fill('harbaugh6@gmail.com');
//   await page.getByPlaceholder('Email address').press('Tab');
//   await page.getByPlaceholder('Password').fill('JessiKyle20!8');
//   await page.getByRole('button', { name: 'Sign in with LeagueApps' }).click();
//   await expect(page.getByText('Welcome back, Kyle')).toBeVisible();
// });

// test('cannot log in with invalid credentials', async ({ page }) => {
//   await page.goto('/');
//   await page.getByRole('link', { name: 'Sign In' }).click();
//   await page.getByPlaceholder('Email address').click();
//   await page.getByPlaceholder('Email address').fill('harbaugh6@gmail.com');
//   await page.getByPlaceholder('Password').click();
//   await page.getByPlaceholder('Password').fill('JessiKyle2020');
//   await page.getByRole('button', { name: 'Sign in with LeagueApps' }).click();
//   await expect(page.getByText('Invalid email or password')).toBeVisible();
// });