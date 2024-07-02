// This test file is to be used to demonstrate an understanding of Playwright and it's abilities.

import { test, expect } from '@playwright/test'
import { zcHomepage } from '../fixtures/zcHomepage.page';

test.describe('Go to Zoomcare homepage', () => {
    let homepage;

    test.beforeEach(async ({page}) => {
        homepage = new zcHomepage(page);
    })

    test('should go to the Zoomcare QA Homepage', async ({page}) => {
        await page.goto('/')
        await homepage.waitForTopNavElements();
    });

    test('clicking the Schedule link should take the user to the Schedule page', async ({page}) => {
        await page.goto('/')
        await homepage.scheduleCTA.click()
    })

    test('filling out the Quick Scheduler should take the user to the correct Schedule page', async ({page}) => {
        //
    })
})