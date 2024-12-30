<template>
  <div class="aircraft-list">
    <!-- Кнопка назад -->
    <div class="back-button">
      <router-link to="/dashboard" class="back-btn">Назад</router-link>
    </div>

    <!-- Фильтрация -->
    <div class="filters">
      <label for="onboard-filter">Фильтр по бортовому номеру:</label>
      <input
          type="text"
          id="onboard-filter"
          v-model="onBoardFilter"
          @input="filterAircraft"
          placeholder="Введите бортовой номер"
      />

      <label for="company-filter">Фильтр по названию компании:</label>
      <input
          type="text"
          id="company-filter"
          v-model="companyFilter"
          @input="filterAircraft"
          placeholder="Введите название компании"
      />
    </div>

    <!-- Таблица самолётов -->
    <table>
      <thead>
      <tr>
        <th>Бортовой номер</th>
        <th>Название компании</th>
        <th>Налет часов</th>
        <th>Дата последнего обслуживания</th>
        <th>Дата выпуска</th>
        <th>Производитель</th>
        <th>Номер модели</th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="aircraft in filteredAircraftList" :key="aircraft.onBoard_number">
        <td>{{ aircraft.onBoard_number }}</td>
        <td>{{ aircraft.company_name.company_name }}</td>
        <td>{{ aircraft.flight_hours }}</td>
        <td>{{ aircraft.last_maintenance_date || 'Не указана' }}</td>
        <td>{{ aircraft.manufacture_date || 'Не указана' }}</td>
        <td>{{ aircraft.model_details.manufacturer }}</td>
        <td>{{ aircraft.model_details.model_number }}</td>
      </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      aircraftList: [], // Исходный список самолётов
      filteredAircraftList: [], // Отфильтрованный список самолётов
      onBoardFilter: "", // Фильтр по бортовому номеру
      companyFilter: "", // Фильтр по названию компании
      token: localStorage.getItem("auth_token"), // Токен для авторизации
    };
  },
  created() {
    this.loadAircraftList();
  },
  methods: {
    // Загрузка списка самолётов с сервера
    async loadAircraftList() {
      try {
        if (!this.token) {
          console.error("Токен не найден. Вы должны быть авторизованы.");
          return;
        }
        const response = await axios.get("/api/aircrafts/", {
          headers: {
            Authorization: `Token ${this.token}`,
          },
        });
        this.aircraftList = response.data;
        this.filteredAircraftList = this.aircraftList; // Изначально показываем всех самолётов
      } catch (error) {
        console.error("Ошибка при загрузке самолётов:", error);
      }
    },
    // Фильтрация списка самолётов
    filterAircraft() {
      this.filteredAircraftList = this.aircraftList.filter((aircraft) => {
        const matchOnBoard = this.onBoardFilter
            ? aircraft.onBoard_number
                .toLowerCase()
                .includes(this.onBoardFilter.toLowerCase())
            : true;
        const matchCompany = this.companyFilter
            ? aircraft.company_name.company_name
                .toLowerCase()
                .includes(this.companyFilter.toLowerCase())
            : true;
        return matchOnBoard && matchCompany;
      });
    },
  },
};
</script>

<style scoped>
.aircraft-list {
  padding: 20px;
}

/* Стили для кнопки назад */
.back-button {
  margin-bottom: 20px;
}

.back-btn {
  background-color: #007bff;
  color: white;
  padding: 10px 20px;
  text-decoration: none;
  border-radius: 5px;
  font-size: 16px;
  cursor: pointer;
}

.back-btn:hover {
  background-color: #0056b3;
}

.filters {
  margin-bottom: 20px;
}

.filters label {
  font-weight: bold;
  margin-right: 10px;
}

.filters input[type="text"] {
  padding: 8px;
  font-size: 1rem;
  border: 1px solid #ccc;
  border-radius: 5px;
  margin-right: 10px;
}

.filters input[type="text"]:focus {
  border-color: #007bff;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
}

th,
td {
  padding: 10px;
  text-align: left;
  border-bottom: 1px solid #ccc;
}

th {
  background-color: #f4f4f4;
}
</style>
