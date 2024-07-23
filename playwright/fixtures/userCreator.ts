import { faker } from '@faker-js/faker/locale/en_US';

interface UserProps {
    /**
    * A random string for first name.
    */
    firstName?: string
    /**
    * A random string for last name.
    */
    lastName?: string
    /**
    * A random email address.
    */
    email?: string
    /**
    * A random string for a password
    */
    password?: string
}

export default class UserCreator implements UserProps {
    firstName: string;
    lastName: string;
    email: string;
    password: string;

    constructor(opts?: UserProps) {
      this.firstName = opts?.firstName || faker.person.firstName();
      this.lastName = opts?.lastName || `${(faker.person.lastName() + "+Test")}`;
      this.email = opts?.email || `${this.firstName}.${this.lastName}@test.com`;
      this.password = opts?.password || `${faker.internet.password()}`;
    }
}