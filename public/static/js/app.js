'use strict';


const config = {
  apiUrl: 'http://127.0.0.1:5000/api',
  gogUrl: 'https://www.gog.com'
};


const GamesList = Vue.component('games-list', {
  template: '#games-list-template',
  props: ['games']
});


const Navbar = Vue.component('navbar-component', {
  template: '#navbar-template',
  props: ['sortBy'],
  data() {
    return {
      isSortMenuVisible: false
    }
  },
  methods: {
    setSortBy: function(sortType) {
      this.$root['sortBy'] = sortType;
      this.toggleSortMenu();
    },
    toggleSortMenu: function() {
      this.isSortMenuVisible
        ? this.isSortMenuVisible = false
        : this.isSortMenuVisible = true;
    }
  }
});


const app = new Vue({
  
  el: '#app',

  data: {
    apiUrl: config.apiUrl,
    gogUrl: config.gogUrl,
    games: [],
    sortBy: 'unsorted',
    isSortMenuVisible: false
  },

  created() {
    this.requestGetGames();
  },

  computed: {
    gamesByTitle: function() {
      return this.games.sort((a, b) => {
        return a.title.localeCompare(b.title);
      });
    },
    gamesByPrice: function() {
      return this.games.sort((a, b) => {
        return a.price.finalAmount - b.price.finalAmount;
      });
    },
    gamesByRating: function() {
      return this.games.sort((a, b) => {
        return b.rating - a.rating;
      });
    },
    getGames: function() {
      /*
        Return games list based on current sort type.
      */
      if (this.sortBy === 'title') { return this.gamesByTitle; }
      if (this.sortBy === 'price') { return this.gamesByPrice; }
      if (this.sortBy === 'rating') { return this.gamesByRating; }
      return this.games;
    }
  },

  methods: {
    requestGetGames: function() {

      let req = new XMLHttpRequest();
      let self = this;

      req.open('GET', this.apiUrl + '/games');
      req.send(null);
      req.onload = () => {
        if (req.status === 200) {
          self.games = JSON.parse(req.response).products;          
        }
      };
    }
  }
});
