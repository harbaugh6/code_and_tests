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
    })
})