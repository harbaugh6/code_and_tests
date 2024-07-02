import {expect, type Page, type Locator} from '@playwright/test'

export class LoginPage {
    public readonly signUpButton: Locator;
    public readonly logInButton: Locator;

    constructor(public readonly page: Page) {
        this.signUpButton = this.page.locator('[id="log_in_button-loginModal.register.logIn"]')
        this.logInButton = this.page.locator('[data-testid="button-loginModal.register.logIn"]')
    }

    async waitForElements() {
        await expect(this.signUpButton).toBeVisible;
        await expect(this.logInButton).toBeVisible;
    }
}