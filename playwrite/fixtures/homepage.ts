import type { Page, Locator } from '@playwright/test'

export class Homepage {
    private readonly signUpLink: Locator;
    private readonly signInLink: Locator;
    public readonly sportsLink: Locator;
    public readonly softballLink: Locator;

    constructor(public readonly page: Page) {
        this.signUpLink = this.page.locator('#account-nav > div > p > a:nth-child(1)');
        this.signInLink = this.page.locator('#account-nav > div > p > a:nth-child(3)');
        this.sportsLink = this.page.locator('#nav > div > div > ul > li.has-sub > a');
        this.softballLink = this.page.locator('#nav > div > div > ul > li.has-sub > dl > dd:nth-child(1) > a');
    }

    async signIn() {
        await this.signInLink.click();
    }

    async goToSoftball() {
        await this.sportsLink.hover();
        await this.softballLink.click();
    }
}