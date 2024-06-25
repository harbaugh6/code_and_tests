import type { Page, Locator } from '@playwright/test'
import {expect} from '@playwright/test'

export class zcHomepage {
    public readonly zoomcareLogo: Locator;
    public readonly scheduleButton: Locator;
    public readonly locationsButton: Locator;
    public readonly servicesButton: Locator;
    public readonly pricingButton: Locator;
    public readonly loginButton: Locator;

    // constructor starts here
    constructor(public readonly page: Page) {
        this.zoomcareLogo = this.page.getByRole('link', {name: 'home'})
        this.scheduleButton = this.page.getByRole('link', {name: 'Schedule'});
        this.locationsButton = this.page.getByRole('link', {name: 'Locations'});
        this.servicesButton = this.page.getByRole('link', {name: 'Services'});
        this.pricingButton = this.page.getByRole('link', {name: 'Pricing & Insurance'});
        this.loginButton = this.page.getByRole('link', {name: 'Login'});
    }

    async waitForTopNavElements() {
        await expect(this.zoomcareLogo).toBeVisible;
        await expect(this.scheduleButton).toBeVisible;
        await expect(this.locationsButton).toBeVisible;
        await expect(this.servicesButton).toBeVisible;
        await expect(this.pricingButton).toBeVisible;
        await expect(this.loginButton).toBeVisible;
    }
}