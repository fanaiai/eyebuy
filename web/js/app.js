'use strict';
angular.module('app.directives', []);
angular.module('app.services', []);
angular.module('app.filters', []);
angular.module('app.controllers', []);
angular.module('app', [
  'app.filters',
  'app.services',
  'app.directives',
  'app.controllers'
])