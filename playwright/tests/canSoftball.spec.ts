import {test, expect } from '@playwright/test'
import {Homepage} from '../fixtures/homepage'

const baseUrl = 'http://capalum.org'

test.describe('CAN Softball', () => {
    test.beforeAll(async ({page}) => {
        await page.goto('about:blank');
    })

    test.beforeEach(async ({page}) => {
        await page.goto(baseUrl);
        await expect(page.getByRole('link', { name: 'Capitol Alumni Network' })).toBeVisible();
    });

    test('should go to the Softball main page', async ({page}) => {
        await page.getByRole('link', {name: '| Sports |'}).hover();
        await page.getByRole('link', {name: 'Softball'}).click();
    });

    test('Goes to the softball standing page', async ({ page }) => {  
        await page.getByRole('link', { name: '| Sports |' }).hover();
        await page.getByRole('link', { name: 'Softball' }).click();
        await page.getByRole('link', { name: 'Teams, Schedule and Standings' }).click();
        await page.getByRole('link', { name: 'Standings' }).click();
      });
})