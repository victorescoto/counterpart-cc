<template>
  <section class="section">
    <form class="box" @submit.prevent="search">
      <div class="columns">
        <div class="field column">
          <label class="label" for="cities">Choose a city</label>
          <div class="control">
            <div class="select">
              <select id="cities" v-model="city" required>
                <option value=""></option>
                <option v-for="city in cities" :key="city.id" :value="city.id">
                  {{ city.name }}
                </option>
              </select>
            </div>
          </div>
        </div>

        <div class="field column">
          <label class="label" for="start-date">Start date</label>
          <div class="control">
            <input
              class="input"
              type="date"
              id="start-date"
              v-model="startDate"
              :max="endDate"
              required
            />
          </div>
        </div>

        <div class="field column">
          <label class="label" for="end-date">End date</label>
          <div class="control">
            <input
              class="input"
              type="date"
              id="end-date"
              v-model="endDate"
              :min="startDate"
              required
            />
          </div>
        </div>
      </div>
      <div class="control">
        <button
          type="submit"
          class="button is-primary"
          :class="{ 'is-loading': loading }"
        >
          Search
        </button>
      </div>
    </form>

    <transition name="fade">
      <div v-if="result" class="box" :class="{ 'is-loading': loading }">
        <h3 class="title is-6">Search Result</h3>
        <p>
          {{ resultFormatted }}
        </p>
      </div>
    </transition>
  </section>
</template>

<script>
import { getCities, doSearch } from "../services/api_service";
import { DateTime } from "luxon";

export default {
  name: "Search",
  data() {
    return {
      loading: false,
      cities: [],
      city: null,
      startDate: null,
      endDate: null,
      result: null,
      resultFormatted: null,
    };
  },
  methods: {
    search() {
      this.loading = true;
      this.result = null;

      doSearch({
        city: this.city,
        startDate: this.startDate,
        endDate: this.endDate,
      }).then(({ data }) => {
        this.loading = false;
        this.result = data;
        this.formatResult();
      });
    },
    formatResult() {
      if (this.result?.detail) {
        this.resultFormatted = this.result.detail;
        return;
      }

      const startDate = DateTime.fromISO(this.startDate).toFormat("LLLL d y");
      const endDate = DateTime.fromISO(this.endDate).toFormat("LLLL d y");
      const earthquakeDate = DateTime.fromMillis(this.result?.time).toFormat("LLLL d y");

      this.resultFormatted = `Result for ${this.result.city_name} between ${startDate} and ${endDate}: The closest Earthquake to ${this.result.city_name} was a ${this.result.title} on ${earthquakeDate}`;
    },
  },
  mounted() {
    getCities().then(({ data }) => (this.cities = data));
  },
};
</script>

<style>
.select,
.select select {
  width: 100%;
}

.fade-enter-active {
  -webkit-animation: fade-in-right 0.6s cubic-bezier(0.39, 0.575, 0.565, 1) both;
  animation: fade-in-right 0.6s cubic-bezier(0.39, 0.575, 0.565, 1) both;
}

.fade-leave-active {
  -webkit-animation: fade-out-right 0.7s cubic-bezier(0.25, 0.46, 0.45, 0.94)
    both;
  animation: fade-out-right 0.7s cubic-bezier(0.25, 0.46, 0.45, 0.94) both;
}

/**
 * ----------------------------------------
 * animation fade-in-right
 * ----------------------------------------
 */
@-webkit-keyframes fade-in-right {
  0% {
    -webkit-transform: translateX(50px);
    transform: translateX(50px);
    opacity: 0;
  }
  100% {
    -webkit-transform: translateX(0);
    transform: translateX(0);
    opacity: 1;
  }
}
@keyframes fade-in-right {
  0% {
    -webkit-transform: translateX(50px);
    transform: translateX(50px);
    opacity: 0;
  }
  100% {
    -webkit-transform: translateX(0);
    transform: translateX(0);
    opacity: 1;
  }
}

/**
 * ----------------------------------------
 * animation fade-out-right
 * ----------------------------------------
 */
@-webkit-keyframes fade-out-right {
  0% {
    -webkit-transform: translateX(0);
    transform: translateX(0);
    opacity: 1;
  }
  100% {
    -webkit-transform: translateX(50px);
    transform: translateX(50px);
    opacity: 0;
  }
}
@keyframes fade-out-right {
  0% {
    -webkit-transform: translateX(0);
    transform: translateX(0);
    opacity: 1;
  }
  100% {
    -webkit-transform: translateX(50px);
    transform: translateX(50px);
    opacity: 0;
  }
}
</style>